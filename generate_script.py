import os
from groq import Groq

# Get Groq API key from environment
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set.")

client = Groq(api_key=api_key)


def generate_reel():
    prompt = """
Create one Instagram Reel for an Indian audience.

Topic:
How to make money online in India.

Requirements:
- 30–45 seconds
- Start with a very strong hook
- Simple Hindi/Hinglish
- Natural and conversational
- Give one practical money-making idea
- No fake income claims
- No mention of AI or automation
- Make it useful for beginners

Return exactly in this format:

HOOK:
[hook]

SCRIPT:
[full voice-over script]

CAPTION:
[Instagram caption]

HASHTAGS:
[10 relevant hashtags]
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8,
        max_tokens=800
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    result = generate_reel()
    print(result)
