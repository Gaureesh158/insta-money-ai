import os
import requests


def download_visual(query, output_file="background.jpg"):
    api_key = os.getenv("PEXELS_API_KEY")

    if not api_key:
        raise ValueError("PEXELS_API_KEY is not set.")

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": api_key
    }

    params = {
        "query": query,
        "per_page": 10,
        "orientation": "portrait"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    photos = data.get("photos", [])

    if not photos:
        raise ValueError(f"No visual found for: {query}")

    # Pick the first suitable result
    photo = photos[0]

    image_url = photo["src"]["large2x"]

    image_response = requests.get(
        image_url,
        timeout=60
    )

    image_response.raise_for_status()

    with open(output_file, "wb") as image_file:
        image_file.write(image_response.content)

    print(f"Visual downloaded: {output_file}")


if __name__ == "__main__":
    download_visual("online business money India")
