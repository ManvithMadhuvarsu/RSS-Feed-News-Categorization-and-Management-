from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base

class Article(Base):
    __tablename__ = 'news_articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text)
    pub_date = Column(DateTime)
    url = Column(String(255))
    category = Column(String(100))

    def __repr__(self):
        return f"<Article(title={self.title}, pub_date={self.pub_date})>"
