from fastapi import Depends
from sqlalchemy import Session, SQLAlchemy, create_engine

from .config import settings

engine = create_engine(
    settings.db.uri,
    echo=settings.db.echo,
    connect_args=settings.db.connect_args,
)


def create_db_and_tables(engine):
    SQLAlchemy.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


ActiveSession = Depends(get_session)
