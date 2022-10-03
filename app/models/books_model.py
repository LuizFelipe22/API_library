import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from .model_base import ModelBase

class Books(ModelBase):
    __tablename__: str = 'books'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    create_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    book: str = sa.Column(sa.String(50), unique=True, nullable=False)
    type: str = sa.Column(sa.String(50), unique=False, nullable=True)
    tags: str = sa.Column(sa.String(50), unique=False, nullable=True)

    modification_date: datetime = sa.Column(sa.DateTime, unique=False, nullable=True)

    def __repr__(self) -> str:
        return f'<Books>'