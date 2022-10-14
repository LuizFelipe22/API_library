from app import app

import csv
from datetime import datetime
from flask import jsonify, request

from app.services.db_insert import create_book, create_tag
from app.services.db_read import read_book, read_tag, read_consult_book


@app.route('/importar-book', methods=['POST'])
def import_book():

    filename = request.json["filename"]
    livros = []

    try:
        with open(filename, "r") as file:
            file_csv = csv.DictReader(file, delimiter=",")

            for linha in file_csv:

                for tag in linha["tag"].split(";"):
                    if read_tag(tag) is None:
                        create_tag(tag)

                if read_consult_book(linha['text']) is None:
                    create_book(book=linha['text'], type=linha['type'], tags=linha['tag'])
                    livros.append(f"O livro '{linha['text']}' foi importado com sucesso.")

                else:
                    livros.append(f"O livro '{linha['text']}' já existe.")

            return jsonify(datetime=datetime.now(),
                           data=livros,
                           status=200)
            
    except FileNotFoundError:
        return jsonify(datetime= datetime.now(),
                       error= "Arquivo não encontrado.",
                       status=404)
