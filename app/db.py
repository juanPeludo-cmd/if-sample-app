from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("sqlite:///sample.db")


class Base(DeclarativeBase):
    pass


def get_session() -> Session:
    return Session(engine)
