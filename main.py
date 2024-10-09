import logging
from database import create_database
from feed_parser import fetch_articles
from classify import categorize_and_store

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of RSS feeds
rss_feeds = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml",
]

if __name__ == "__main__":
    try:
        create_database()
        fetch_articles(rss_feeds)
        categorize_and_store()
        logging.info("News article collection and categorization completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
