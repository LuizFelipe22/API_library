import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from .model_base import ModelBase


class Tags(ModelBase):
    __tablename__: str = 'tags'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    create_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    tag: str = sa.Column(sa.String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Tags>'