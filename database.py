from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'mysql+pymysql://root:manvith9935@localhost/project'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Start session
Session = sessionmaker(bind=engine)
session = Session()

def create_database():
    Base.metadata.create_all(engine)
