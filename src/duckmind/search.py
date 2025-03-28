import logging
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from duckduckgo_search import DDGS

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Search:
    def __init__(self):
        pass

    @staticmethod
    def extract_content_from_url(url):
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the HTML content
            html_content = response.text

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # For example, you can extract all text:
            text = soup.get_text()

            # Or, you can extract specific elements. For instance, extracting all <p> tags:
            paragraphs = soup.find_all('p')
            result = ''
            for p in paragraphs:
                result += p.get_text() + '\n'

            return result
        else:
            print("Failed to retrieve the webpage:", response.status_code)

    def summarize_contents(self, url_list: list, is_ddg: bool = True) -> str:
        from ai_manager import AIGenerator
        ai_client = AIGenerator()
        search_results = []

        for url in url_list:
            # Extract full content from the URL
            url_full_content = self.extract_content_from_url(url)

            if url_full_content:
                prompt = f"""Generate a summary of the following content:
                {url_full_content}"""
                if is_ddg:
                    # Use the DuckDuckGo API for summarization
                    summary = ai_client.generate_ddg(prompt)
                else:
                    # Use the Groq API for summarization
                    summary = ai_client.generate(prompt)
                search_results.append(summary)

        return "\n\n".join(search_results)

    @staticmethod
    def merge_contents(contents: str, is_ddg: bool = True) -> str:
        from ai_manager import AIGenerator
        prompt = f"""Merge the following contents into a single coherent text: 
        {contents}"""

        ai_client = AIGenerator()
        if is_ddg:
            # Use the DuckDuckGo API for merging
            return ai_client.generate_ddg(prompt)
        else:
            # Use the Groq API for merging
            return ai_client.generate(prompt)

    def search_google(self, query: str) -> str | None:
        """
        Perform a Google search using the googlesearch module.
        Note: This method returns a list of result URLs instead of scraped snippets.

        Args:
            query (str): The search query.

        Returns:
            str: A string containing search result URLs separated by newlines.
        """
        try:
            url_list = list(search(query, num_results=3))

            # check if urls are valid
            for url in url_list:
                if not url.startswith('http'):
                    url_list.remove(url)

            summarized_results = self.summarize_contents(url_list, is_ddg=False)
            return self.merge_contents(summarized_results, is_ddg=False) if len(url_list) > 1 else summarized_results

        except Exception as e:
            logger.error("Error with Google search: %s", e)
            raise

    def search_ddg(self, query: str) -> str:
        """
        Perform a search query using the DuckDuckGo API.

        Args:
            query (str): The search query.

        Returns:
            str: The search result snippets.
        """
        try:
            with DDGS() as ddgs:
                results = ddgs.text(query, region='wt-wt', safesearch='off', timelimit=None, max_results=5)
            url_list = [result.get('href', '') for result in results if result.get('href')]
            summarized_results = self.summarize_contents(url_list)
            return self.merge_contents(summarized_results) if len(url_list) > 1 else summarized_results

        except Exception as e:
            logger.error("Error with DuckDuckGo search: %s", e)
            raise
