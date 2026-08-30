import os
import requests


def generate_voice(text, output_file="voice.mp3"):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = os.getenv("ELEVENLABS_VOICE_ID")

    if not api_key:
        raise ValueError("ELEVENLABS_API_KEY is not set.")

    if not voice_id:
        raise ValueError("ELEVENLABS_VOICE_ID is not set.")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=120
    )

    response.raise_for_status()

    with open(output_file, "wb") as audio_file:
        audio_file.write(response.content)

    print(f"Voice generated: {output_file}")


if __name__ == "__main__":
    script_file = "script.txt"

    if not os.path.exists(script_file):
        raise FileNotFoundError("script.txt not found.")

    with open(script_file, "r", encoding="utf-8") as file:
        script = file.read().strip()

    if not script:
        raise ValueError("script.txt is empty.")

    generate_voice(script)
