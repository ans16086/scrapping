import requests
from bs4 import BeautifulSoup

def get_youtube_subscribers(channel_name):
    search_url = f"https://www.youtube.com/{channel_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    # Make request to YouTube search results page
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the first search result
    channel_link = soup.find("a", {"href": lambda href: href and "/channel/" in href})

    if not channel_link:
        return {"error": "Channel not found"}

    channel_url = f"https://www.youtube.com{channel_link['href']}"
    
    # Scrape channel page for subscribers
    response = requests.get(channel_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    subscriber_tag = soup.find("yt-formatted-string", {"id": "subscriber-count"})
    
    if subscriber_tag:
        subscribers = subscriber_tag.text.strip()
        return {"channel": channel_name, "subscribers": subscribers}
    else:
        return {"error": "Unable to retrieve subscribers"}
