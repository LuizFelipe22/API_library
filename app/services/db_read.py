from app.database.db_session import create_session
from app.models.books_model import Books
from app.models.tags_model import Tags


def read_book(book_id: str):
    with create_session() as session:
        book = session.query(Books).filter(Books.id == book_id).first()

    if book == None:
        return None

    return {"id":book.id, "data_de_criacão":book.create_date, "livro":book.book, 
            "tipo":book.type, "tags":book.tags, "data_de_modificação":book.modification_date}

def read_consult_book(book: str):
    with create_session() as session:
        book = session.query(Books).filter(Books.book == book).first()

    if book == None:
        return None

    return {"id":book.id, "data_de_criacão":book.create_date, "livro":book.book, 
            "tipo":book.type, "tags":book.tags, "data_de_modificação":book.modification_date}


def read_book_all():
    with create_session() as session:
        books = session.query(Books)

    if books == None:
        return None

    return [{"id":book.id, "data_de_criacão":book.create_date, 
            "book":book.book, "tipo":book.type, "tags":book.tags, 
            "data_de_modificação":book.modification_date}
             for book in books]


def read_book_all_export():
    with create_session() as session:
        books = session.query(Books)

    if books == None:
        return None

    return [{"book":book.book, "tipo":book.type, "tags":book.tags}
             for book in books]


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
                lista_book.append({"id":i.id, "data_de_criacão":i.create_date, 
            "livro":i.book, "tipo":i.type, "tags":i.tags, "data_de_modificação":i.modification_date})

    return lista_book


def read_tag(id: str):

    lista_tags = []

    for tag in id.split(";"):
        with create_session() as session:
            tag = session.query(Tags).filter(Tags.id == int(tag)).first()

        if tag == None:
            return None

        lista_tags.append({"id":tag.id, "data de criação":tag.create_date , "tag":tag.tag})

    return lista_tags


def read_tag_all():
    with create_session() as session:
        tags = session.query(Tags)

    return [{"id":tag.id, "data de criação":tag.create_date , "tag":tag.tag} for tag in tags]
