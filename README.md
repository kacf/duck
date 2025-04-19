# DuckMind

**Generative AI Templates to Quickly Prototype Applications Using Large Language Models (LLMs) and Real-time Web Search**

---

## Overview

DuckMind provides developers with an easy-to-use template for rapidly building AI-driven applications. It seamlessly integrates popular large language models (LLMs) with real-time search capabilities, enabling quick prototyping without complex API setups or manual integration efforts.

DuckMind supports two primary LLM APIs:

- [DuckDuckGo ChatAI](https://github.com/deedy5/duckai): Free, no API key required.
- [GROQ](https://console.groq.com/docs/overview): Requires an API key.

These APIs are unified under a single interface, making it easy to switch between different models. For detailed model information, see:

- [DuckDuckGo ChatAI models](https://github.com/deedy5/duckai?tab=readme-ov-file#1-chat---ai-chat)
- [GROQ models](https://console.groq.com/docs/models)

Additionally, DuckMind includes built-in real-time web search integration using Google and DuckDuckGo, even for models without native search capabilities.

---

## Features

- **Free and Easy Setup:** Quickly start prototyping without upfront costs (GROQ requires an API key).
- **Unified LLM Interface:** Easily switch between multiple models like GPT, Llama, and others through a simple, consistent API.
- **Live Web Search:** Integrate real-time search results into your AI-generated responses.
- **Modular Design:** Clearly separated AI generation and search functionalities for easy customization.

---

## Requirements

- Python 3.12
- (Optional) [GROQ API Key](https://console.groq.com/docs/overview) if using GROQ. Otherwise, you can utilize the DuckDuckGo ChatAI API without any API keys.

---

## Installation

To set up DuckMind, follow the installation instructions provided in [ENV-README.md](ENV-README.md).

---

## Quick Start

Run DuckMind with the following command:

```bash
python main.py
```

This will launch the DuckMind application, enabling immediate interactions with your chosen AI models and integrated web searches.

---

## Usage Examples

### DuckDuckGo ChatAI Example:

```python
from ai_manager import AIGenerator

ai_client = AIGenerator()

response = ai_client.generate_ddg("News of the day in Italy", model="o3-mini", has_search=True)
print(response)
```

### GROQ API Example:

Set your GROQ API key as an environment variable named `GROQ_API_KEY`, then use the following snippet:

```python
from ai_manager import AIGenerator

ai_client = AIGenerator()

response = ai_client.generate("News of the day in Italy", model="qwen-qwq-32b", has_search=True)
print(response)
```

---

## Contributing

We welcome contributions! To get involved:

- Open an issue to discuss ideas or report bugs.
- Fork the repository and submit a pull request.

Ensure your contributions are clearly documented and thoroughly tested.

---

## License

DuckMind is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Disclaimer
This library is not affiliated with DuckDuckGo and is for educational purposes only. It is not intended for commercial 
use or any purpose that violates DuckDuckGo's Terms of Service. By using this library, you acknowledge that you will 
not use it in a way that infringes on DuckDuckGo's terms. The official DuckDuckGo website can be found 
at https://duckduckgo.com.

---

Special thanks to [DuckDuckGo](https://duckduckgo.com/), [Groq](https://console.groq.com/docs/overview), and [duckduckgo-search by deedy5](https://pypi.org/project/duckduckgo-search/) for their fantastic resources.

Happy prototyping with DuckMind!
