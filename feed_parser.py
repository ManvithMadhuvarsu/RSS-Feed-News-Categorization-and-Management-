from datetime import datetime
import feedparser
import logging
from models import Article
from database import session

def fetch_articles(feed_urls):
    for url in feed_urls:
        logging.info(f"Fetching articles from {url}")
        feed = feedparser.parse(url)

        for entry in feed.entries:
            title = entry.title
            content = getattr(entry, 'summary', None)
            if content is None:
                if 'content' in entry and isinstance(entry.content, list):
                    content = entry.content[0].value
                else:
                    content = ''

            pub_date_str = getattr(entry, 'published', None)
            if pub_date_str:
                try:
                    pub_date = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %Z')
                except ValueError as e:
                    logging.error(f"Date parsing error for article '{title}': {e}")
                    pub_date = None
            else:
                logging.warning(f"No published date found for article '{title}', skipping...")
                pub_date = None
            url = getattr(entry, 'link', None)

            # Check for duplicates
            if not session.query(Article).filter_by(title=title).first():
                if pub_date is not None:
                    article = Article(title=title, content=content, pub_date=pub_date, url=url, category='')
                    session.add(article)
                    logging.info(f"Added article: {title}")
                else:
                    logging.warning(f"Skipping article '{title}' due to missing published date.")

    session.commit()
