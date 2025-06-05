import os
import logging
import openai
from duckai import DuckAI
from search import Search
from utils import remove_think_tags

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class AIGenerator:
    """
    A unified class to interact with the OpenAI API via Groq for generating text.
    """

    def __init__(self) -> None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        self.client = openai.OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=api_key
        )

    def generate(self, prompt: str, model: str = "llama-3.3-70b-versatile", role: str = "user",
                 temperature: float = 0.7, has_search: bool = False, is_printing_cot: bool = True) -> str:
        """
        Generates text based on the provided prompt using the OpenAI API.
        Models list: https://console.groq.com/docs/models

        Args:
            prompt (str): The input text prompt.
            model (str, optional): The model to use. Defaults to "llama-3.3-70b-versatile".
            role (str, optional): The role of the message (e.g., "user"). Defaults to "user".
            temperature (float, optional): Temperature setting for text generation. Defaults to 0.7.
            has_search (bool, optional): Whether to include search results in the prompt. Defaults to False.
            is_printing_cot (bool, optional): Whether to include the "Printing Chain of Thoughts" (COT) in the prompt.

        Returns:
            str: The generated text.
        """
        try:
            if has_search:
                search_results = Search().search_google(prompt)
                prompt = f"{prompt}\n\n<search>\n{search_results}\n</search>"
            chat_completion = self.client.chat.completions.create(
                messages=[{"role": role, "content": prompt}],
                model=model,
                temperature=temperature
            )
            return chat_completion.choices[0].message.content if is_printing_cot \
                else remove_think_tags(chat_completion.choices[0].message.content)
        except Exception as e:
            logger.error("Error generating text: %s", e)
            raise

    @staticmethod
    def generate_ddg(keywords: str, model: str = "gpt-4o-mini", has_search: bool = False) -> str:
        """
        Initiates a chat session with DuckDuckGo AI.
        Models list: https://pypi.org/project/duckduckgo-search/

        Args:
            keywords (str): The initial message or question to send to the AI.
            model (str): The model to use: "gpt-4o-mini", "llama-3.3-70b", "claude-3-haiku",
                "o3-mini", "mistral-small-3". Defaults to "gpt-4o-mini".
            has_search (bool, optional): Whether to include search results in the prompt. Defaults to False.

        Returns:
            str: The response from the AI.
        """
        try:
            if has_search:
                search_results = Search().search_google(keywords)
                keywords = f"{keywords}\n\n<search>\n{search_results}\n</search>"
            with DuckAI() as dai:
                response = dai.chat(keywords, model=model)
            return response
        except Exception as e:
            logger.error("Error with DuckDuckGo AI chat: %s", e)
            raise
