from email.policy import default
from app import app

from flask import request, jsonify

from app.services.db_insert import create_book
from app.services.db_read import read_book, read_book_all, read_tag, read_book_tags, read_consult_book
from app.services.db_update import update_book
from app.services.db_delete import delete_book

from datetime import datetime


@app.route('/livro', methods=['POST'])
def addbook():

    book = request.json['book']
    tipo = request.json['type']
    tags = request.json['tags']

    if read_consult_book(book) != None: 
        return jsonify(datetime= datetime.now(),
                       error= f"O livro '{book}' já estar cadastrado.",
                       status=400)

    for tag in tags.split(";"):
        if read_tag(tag) is None:
            return jsonify(datetime= datetime.now(),
                           error= f"A tag '{tag}' não foi encontrada.",
                           status=400)

    create_book(book, tipo, tags)

    return jsonify(datetime= datetime.now(),
                   message= "Livro adicionado com sucesso!!",
                   status=201)


@app.route('/livro', defaults={'id': None})
@app.route('/livro/<int:id>')
def book(id: str):

    if id:
        consultar = read_book(id)
        if consultar == None:
            return jsonify(datetime= datetime.now(),
                           error= f"Não encontramos o ID '{id}'.",
                           status=404)

    elif id is None:
        consultar = read_book_all()

    return jsonify(datetime= datetime.now(),
                   data= consultar,
                   status=200)


@app.route('/livro/<int:id>', methods=['PUT'])
def put_book(id: int):

    tags = request.json['tags']
    book = request.json['book']
    type = request.json['type']

    if book == read_book(id)['livro']:
        pass

    elif read_consult_book(book) != None: 
        return jsonify(datetime= datetime.now(),
                       error= f"O livro '{book}' já estar cadastrado.",
                       status=400)

    for tag in tags.split(";"):
        if read_tag(tag) is None:
            return jsonify(datetime= datetime.now(),
                           error= f"A tag '{tag}' não foi encontrada.",
                           status=400)

    update_book(id, book, tags, type)

    return jsonify(datetime= datetime.now(),
                   message= "Edição concluída.",
                   status=201)

    
@app.route('/livro/<int:id>', methods=['DELETE'])
def del_book(id: int):

    if delete_book(id) is None:
        return jsonify(datetime= datetime.now(),
                       error= "Este Livro não foi encontrado em nosso banco de dados.",
                       status=404)

    return jsonify(datetime= datetime.now(),
                   message= f"Livro com o id '{id}' foi excluído.",
                   status=202)

@app.route('/livro/tag', defaults={"tags": None})
@app.route('/livro/tag/<tags>')
def consult_by_tags(tags: str):

    if tags == None:
        return jsonify(datetime= datetime.now(),
                       error= "Adicione uma tag para consultar.",
                       status=404)

    return jsonify(datetime= datetime.now(),
                   data= read_book_tags(tags),
                   status=200)
