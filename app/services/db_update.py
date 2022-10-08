from app.database.db_session import create_session
from app.models.books_model import Books
from datetime import datetime


def update_book(id: int, new_book: str, new_tags: str, new_type: str):
    with create_session() as session:
        consulta: Books = session.query(Books).filter(Books.id == id).one_or_none()

        if consulta is None: 
            return consulta

        consulta.tags = new_tags
        consulta.book = new_book
        consulta.type = new_type
        consulta.modification_date = datetime.now()


        session.commit()
