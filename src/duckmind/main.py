from ai_manager import AIGenerator

ai_client = AIGenerator()

# Example usage of the AIGenerator using Duckai
response = ai_client.generate_ddg(f"""News of the day in Italy""", model="o3-mini", has_search=True)

# Example usage of the AIGenerator using Groq API (needs GROQ_API_KEY environment variable set)
response = ai_client.generate(f"""News of the day in Italy""", model="qwen/qwen3-32b", has_search=True,
                              is_printing_cot=False)

print(response)
