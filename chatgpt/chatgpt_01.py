from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the environment file (make sure path is correct)
load_dotenv("dev.env")

# Now you can access variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize client with API key
client = OpenAI(api_key=api_key)  # Replace with your key

# Input prompt
user_input = "tell me in 20 words what is water?"

# Create a response
response = client.chat.completions.create(
    model="gpt-4.1-mini",  # You can change to gpt-4.1, gpt-4.1-mini, or gpt-3.5-turbo
    messages=[
        {"role": "user", "content": user_input}
    ]
)

answer = response.choices[0].message.content
# Print the output
print(answer)