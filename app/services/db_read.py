from ctypes.wintypes import tagSIZE
from app.database.db_session import create_session
from app.models.books_model import Books
from app.models.tags_model import Tags


def read_book(book: str):
    with create_session() as session:
        book = session.query(Books).filter(Books.book == book).first()

    if book == None:
        return None

    return [book.book, book.type, book.tags]


def read_book_all():
    with create_session() as session:
        books = session.query(Books)

    if books == None:
        return None

    return [{"Book":book.book, "Tipo":book.type, "Tags":book.tags} for book in books]


def read_book_tag(tag: str):
    
    with create_session() as session:
        books_tag = session.query(Books).filter(Books.tags.ilike('%' + tag + '%'))

    if books_tag == None:
        return None
    
    return [an.book for an in books_tag]

def read_book_tags(tags: str):

    lista_book = []

    for tag in tags.split(";"):
        with create_session() as session:
            books_tag = session.query(Books).filter(Books.tags.ilike('%' + tag + '%'))

        if books_tag != None:
            for i in books_tag:
                lista_book.append(i.book)

    return list(set(lista_book))


def read_tag(tags: str):

    lista_tags = []

    for tag in tags.split(";"):
        with create_session() as session:
            tag = session.query(Tags).filter(Tags.tag == tag).first()

        if tag == None:
            return None

        lista_tags.append(tag.tag)

    return lista_tags


def read_tag_all():
    with create_session() as session:
        tags = session.query(Tags)

    return [{"id": tag.id, "tag":tag.tag} for tag in tags]
