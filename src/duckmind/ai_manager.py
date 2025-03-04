import os
import logging
import openai
from duckduckgo_search import DDGS
from search import Search

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
                 temperature: float = 0.7, search_enabled: bool = False) -> str:
        """
        Generates text based on the provided prompt using the OpenAI API.
        Models list: https://console.groq.com/docs/models

        Args:
            prompt (str): The input text prompt.
            model (str, optional): The model to use. Defaults to "llama-3.3-70b-versatile".
            role (str, optional): The role of the message (e.g., "user"). Defaults to "user".
            temperature (float, optional): Temperature setting for text generation. Defaults to 0.7.

        Returns:
            str: The generated text.
        """
        try:
            if search_enabled:
                search_results = Search().search_google(prompt)
                prompt = f"{prompt}\n\nContext from live search:\n{search_results}"
            chat_completion = self.client.chat.completions.create(
                messages=[{"role": role, "content": prompt}],
                model=model,
                temperature=temperature
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            logger.error("Error generating text: %s", e)
            raise

    @staticmethod
    def generate_ddg(keywords: str, model: str = "gpt-4o-mini", search_enabled: bool = False) -> str:
        """
        Initiates a chat session with DuckDuckGo AI.
        Models list: https://pypi.org/project/duckduckgo-search/

        Args:
            keywords (str): The initial message or question to send to the AI.
            model (str, optional): The model to use. Options include "gpt-4o-mini", "llama-3.3-70b",
                                   "claude-3-haiku", "o3-mini", "mistral-small-3". Defaults to "gpt-4o-mini".

        Returns:
            str: The response from the AI.
        """
        try:
            if search_enabled:
                search_results = Search().search_google(keywords)
                keywords = f"{keywords}\n\nContext from live search:\n{search_results}"
            with DDGS() as ddgs:
                response = ddgs.chat(keywords, model=model)
            return response
        except Exception as e:
            logger.error("Error with DuckDuckGo AI chat: %s", e)
            raise
