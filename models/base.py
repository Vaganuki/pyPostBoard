import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase, sessionmaker


class Base(MappedAsDataclass, DeclarativeBase):
    pass

load_dotenv()

url = os.getenv("DATABASE_URL")
engine = create_engine(url = url)
Session = sessionmaker(bind=engine)