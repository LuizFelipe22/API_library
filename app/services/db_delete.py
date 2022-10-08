from app.database.db_session import create_session
from app.models.books_model import Books
from app.models.tags_model import Tags


def delete_book(id: int):
    with create_session() as session:
        consulta: Books = session.query(Books).filter(Books.id == id).one_or_none()

    if consulta != None:
        session.delete(consulta)
        session.commit()

    return consulta


def delete_tag(id: int):
    with create_session() as session:
        consulta: Tags = session.query(Tags).filter(Tags.id == id).one_or_none()

    if consulta != None:
        session.delete(consulta)
        session.commit()

    return consulta
