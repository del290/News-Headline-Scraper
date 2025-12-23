import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Set your keyword here
keyword = "Apple"  # Change this to whatever you want

# Dictionary of news sources and their headline tags
news_sources = {
    "BBC": {"url": "https://www.bbc.com/news", "tag": "h2"},
    "Fox News": {"url": "https://www.foxnews.com", "tag": "h3"},
    "NPR": {"url": "https://www.npr.org", "tag": "h3"}
}  # ADD THIS CLOSING BRACE


def scrape_headlines(source_name, url, tag, keyword):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all(tag)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n{'=' * 50}")
        print(f"Scraping {source_name} - {current_time}")
        print(f"{'=' * 50}")
        print(f"Found {len(headlines)} total headlines")
        print(f"Searching for '{keyword}'...\n")

        matching_headlines = []
        count = 0

        for headline in headlines:
            text = headline.get_text(strip=True)
            if keyword.lower() in text.lower():
                count += 1
                print(f"{count}. {text}\n")
                matching_headlines.append(f"[{source_name}] {text}")  # Add source name

        if count == 0:
            print(f"No headlines found containing '{keyword}'")
        else:
            print(f"Total matches: {count}")

        return matching_headlines

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {source_name}: {e}")
        return []


# Main loop
seen_headlines = set()

print("Starting multi-source scraper... (Press Ctrl+C to stop)")
print("Checking every minute for new headlines...\n")

while True:
    all_current_headlines = []

    # Loop through each news source
    for source_name, source_info in news_sources.items():
        headlines = scrape_headlines(
            source_name,
            source_info["url"],
            source_info["tag"],
            keyword
        )
        all_current_headlines.extend(headlines)

    # Check for new headlines
    new_headlines = [h for h in all_current_headlines if h not in seen_headlines]

    if new_headlines:
        print("\n🚨 NEW HEADLINES ALERT! 🚨")
        for headline in new_headlines:
            print(f"  • {headline}")
        print()

    # Update seen headlines
    seen_headlines.update(all_current_headlines)

    print("\nWaiting 1 minute before next check...")
    time.sleep(60)