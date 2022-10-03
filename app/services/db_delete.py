from app.database.db_session import create_session
from app.models.books_model import Books
from app.models.tags_model import Tags


def delete_book(book: str):
    with create_session() as session:
        consulta: Books = session.query(Books).filter(Books.book == book).one_or_none()

    if consulta != None:
        session.delete(consulta)
        session.commit()

    return consulta


def delete_tag(tag: str):
    with create_session() as session:
        consulta: Tags = session.query(Tags).filter(Tags.tag == tag).one_or_none()

    if consulta != None:
        session.delete(consulta)
        session.commit()

    return consulta
