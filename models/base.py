import os
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass

load_dotenv()

url = os.getenv("DATABASE_URL")
engine = create_engine(url = url, echo=True)
session_local = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine,
    expire_on_commit = False,
)

def init_db(delete=False):
    if delete:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

@contextmanager
def get_db_session():
    session = session_local()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()