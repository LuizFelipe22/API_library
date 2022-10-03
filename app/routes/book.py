from app import app

from flask import request

from app.services.db_insert import create_book
from app.services.db_read import read_book, read_book_all, read_tag
from app.services.db_update import update_book
from app.services.db_delete import delete_book

from app.services.db_read import read_book_tag, read_book_tags


@app.route('/criar-livro', methods=['POST'])
def addbook():

    book = request.form['book']
    tipo = request.form['type']
    tags = request.form['tags']

    if read_book(book) != None: return {"error": f'O livro {book} já estar cadastrado.'}

    for tag in tags.split(";"):
        if read_tag(tag) is None:
            return {"error": f'A tag {tag} não foi encontrada.'}


    create_book(book, tipo, tags)

    return {"mensagem": 'Livro adicionado com sucesso!!'}


@app.route('/livro', defaults={'book': None})
@app.route('/livro/<book>')
def book(book):

    if book:
        consultar = read_book(book)
        if consultar == None:
            return {"mensagem": f'O livro {book} não existe em nosso banco de dados.'}

    elif book is None:
        consultar = read_book_all()

    return consultar


@app.route('/editar-livro/<book>', methods=['PUT'])
def put_book(book):

    new_tags = request.form['new_tags']
    new_book = request.form['new_book']
    new_type = request.form['new_type']

    if read_book(new_book) != None: return {"error": f'O livro {new_book} já estar cadastrado.'}

    for tag in new_tags.split(";"):
        if read_tag(tag) is None:
            return {"error": f'A tag {tag} não foi encontrada.'}

    update_book(book, new_book, new_tags, new_type)

    return {"mensagem": 'Edição concluída.'}

    
@app.route('/del-livro/<book>', methods=['DELETE'])
def del_book(book):

    if delete_book(book) is None:
        return {"error": 'Este Livro não foi encontrado em nosso banco de dados.'}

    return {"mensagem": 'Livro excluído.'}


@app.route('/consultar-livro-tag/<tags>', methods=['GET'])
def consult_by_tags(tags: str):

    return read_book_tags(tags)
