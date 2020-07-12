import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.orm import sessionmaker
from app.models import create_db
from app.models.Orders import Orders
from app.models.Products import Products


load_dotenv(find_dotenv())

Session = sessionmaker(bind=create_db())
session = Session()
