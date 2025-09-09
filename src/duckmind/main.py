from ai_manager import AIGenerator

ai_client = AIGenerator()

# Example usage of the AIGenerator using Duckai
response = ai_client.generate_ddg(
    """News of the day in Italy""",
    model="o3-mini",
    has_search=True
)

print(response)
