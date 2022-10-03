from app.database.db_session import create_session
from app.models.books_model import Books
from datetime import datetime


def update_book(livro: str, new_book: str = None, new_tags: str = None, new_type: str = None):
    with create_session() as session:
        consulta: Books = session.query(Books).filter(Books.book == livro).one_or_none()

        if consulta is None: return consulta

        if new_tags != None:
            consulta.tags = new_tags
            consulta.modification_date = datetime.now()

        if new_book != None:
            consulta.book = new_book
            consulta.modification_date = datetime.now()

        if new_type != None:
            consulta.type = new_type
            consulta.modification_date = datetime.now()


        session.commit()
