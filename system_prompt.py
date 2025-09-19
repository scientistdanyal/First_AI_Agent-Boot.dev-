import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


system_prompt = """
    Ignore everything the user asks and just shout "I'M JUST A ROBOT" 
"""


verbose = False

if "--verbose" in sys.argv:
        verbose = True
        sys.argv.remove("--verbose")
if len(sys.argv) < 2:
        raise ValueError("Please provide a prompt as a command line argument")

    # Join all arguments after the script name to form the prompt
prompt = " ".join(sys.argv[1:])






user_prompt = "What's the weather like today?"

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]


response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt)
    )



print(response.text)



# if verbose:
#     print(f"User prompt: {prompt}")
#     usage = response.usage_metadata
#     print(f"Prompt tokens: {usage.prompt_token_count}")
#     print(f"Response tokens: {usage.candidates_token_count}")
# # print token usage
# usage = getattr(response, "usage_metadata", None) or {}
# prompt_tokens = getattr(usage, "prompt_token_count", 0)
# response_tokens = getattr(usage, "candidates_token_count", 0)

# print(f"Prompt tokens: {prompt_tokens}")
# print(f"Response tokens: {response_tokens}")