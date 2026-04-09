import os
from dotenv import load_dotenv
import litellm
import logging

# Turn on debug for litellm
litellm._turn_on_debug()

load_dotenv()

litellm.api_base = os.getenv("OPENAI__API_BASE")
litellm.api_key = os.getenv("OPENAI__KEY")

test_model = os.getenv("CONFIG__MODEL")

print(f"Testing model: {test_model}")
print(f"API Base: {litellm.api_base}")

try:
    response = litellm.completion(
        model=test_model,
        messages=[{"role": "user", "content": "Hello!"}],
        max_tokens=10,
    )
    print("Success:", response.choices[0].message.content)
except Exception as e:
    print(f"Error: {repr(e)}")
