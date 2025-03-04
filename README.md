# DuckMind

**DuckMind** is a Python project that provides an easy way to integrate large language models (LLMs) via API for free, along with live search capabilities to bring up-to-date information directly into your code. The project simplifies LLM usage, allowing you to leverage both AI text generation and live search results seamlessly.

## Overview

DuckMind unifies interaction with various LLM APIs and enables real-time web search integration using both Google and DuckDuckGo. This tool is ideal for developers who want to prototype AI applications quickly without dealing with multiple API integrations or manual live data sourcing.

## Features

- **Unified LLM API Integration:** Easily access multiple LLM models such as GPT, Llama, and others via a single interface.
- **Live Search Integration:** Automatically fetch and summarize current information from online search engines (Google and DuckDuckGo).
- **Modular Design:** Clear separation between the AI generator and search functionalities.
- **Free API Access:** Designed for free usage during development (ensure you have the appropriate API keys set up for Groq).

## Requirements

- Python 3.12 
- If you want use Groq you need an API key for accessing the LLM service via [GROQ](https://api.groq.com) instead you can use DuckDuckGo ChatAI API

## Installation

1. Clone the repository:

```bash
git clone
```

2. Create a new Python environment and install the required packages:

```bash
python3 -m venv duckmind
source duckmind/bin/activate
pip install -r requirements.txt
```

3. Set up the environment in your IDE:

## Usage

To use DuckMind, you can run the following command:

```bash
python main.py
```

This will start the DuckMind application, allowing you to interact with the AI models and perform live searches.

## Contributing
Contributions to DuckMind are welcome! If you have suggestions, bug fixes, or new features, please:

* Open an issue to discuss your ideas.
* Fork the repository and submit a pull request.

Make sure your changes are well documented and tested.

# License
This project is licensed under the MIT License. See the LICENSE file for more information.

# Disclaimer
DuckMind integrates external APIs and live search features. Please adhere to the terms of service for any third-party API you use. The project creator is not responsible for any misuse or unexpected behavior arising from these integrations.

Enjoy building your AI-powered applications with DuckMind!
