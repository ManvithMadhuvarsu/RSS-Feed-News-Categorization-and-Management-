import logging
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from models import Article
from database import session

# Sample training data
train_data = [
    ("terrorism protest in city center", "Terrorism / Protest / Political Unrest / Riot"),
    ("community uplifted by new programs", "Positive / Uplifting"),
    ("flooding caused by heavy rains", "Natural Disasters"),
    ("scientists discover new species", "Positive / Uplifting"),
    ("riot breaks out in the streets", "Terrorism / Protest / Political Unrest / Riot"),
    ("earthquake hits the region", "Natural Disasters"),
    ("economic growth on the rise", "Positive / Uplifting"),
    ("no significant news today", "Others"),
]

# Separate the training data into texts and labels
texts, labels = zip(*train_data)

# Create a pipeline that combines a CountVectorizer with a Naive Bayes classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(texts, labels)

# Function to classify articles based on their content
def classify_article(content):
    category = model.predict([content])[0]
    return category

def categorize_and_store():
    articles = session.query(Article).all()
    for article in articles:
        if article.category is None or article.category == "":
            article.category = classify_article(article.content)
            session.commit()
            logging.info(f"Categorized article: '{article.title}' as '{article.category}'")
