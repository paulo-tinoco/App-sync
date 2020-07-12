import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_db():
    engine = create_engine(os.environ.get('DATABASE_URI'), echo=False)

    Base.metadata.create_all(bind=engine)

    return engine