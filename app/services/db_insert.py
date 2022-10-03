from app.database.db_session import create_session

from app.models.books_model import Books
from app.models.tags_model import Tags


def create_book(book, type=None, tags=None):

    new_book: Books = Books(book=book,type=type,tags=tags)

    with create_session() as session:
        session.add(new_book)
        session.commit()


def create_tag(tags):

    for tag in tags.split(";"):
        new_tag: Tags = Tags(tag=tag)

        with create_session() as session:
            session.add(new_tag)
            session.commit()