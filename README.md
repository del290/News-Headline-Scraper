# Multi-Source News Headline Scraper

A Python web scraper that monitors news headlines from BBC, Fox News, and NPR, and alerts you when new articles matching your keywords appear.

## Features

- 🔍 Scrapes headlines from multiple news sources
- 🎯 Filters by custom keywords
- 🔔 Alerts when new matching headlines are found
- ⏰ Runs automatically at set intervals
- 🏷️ Tags headlines with their source

## Requirements

- Python 3.x
- requests
- beautifulsoup4

## Installation
```bash
pip install requests beautifulsoup4
```

## Usage

1. Set your keyword in the script:
```python
keyword = "your_keyword"
```

2. Run the scraper:
```bash
python scraper.py
```

3. Press Ctrl+C to stop

## How to Add More Sources

Inspect the website's HTML to find headline tags, then add to `news_sources`:
```python
"Source Name": {"url": "https://example.com", "tag": "h2"}
```
