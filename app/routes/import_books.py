from app import app

import csv
from datetime import datetime
from flask import jsonify, request

from app.services.db_insert import create_book, create_tag
from app.services.db_read import read_book, read_tag


@app.route('/importar-book', methods=['POST'])
def import_book():

    filename = request.json['filename']

    try:
        with open(filename, "r") as file:
            file_csv = csv.DictReader(file, delimiter=",")

            for linha in file_csv:

                for tag in linha['tag'].split(";"):
                    if read_tag(tag) is None:
                        create_tag(tag)

                if read_book(linha['text']) is None:
                    create_book(book=linha['text'], type=linha['type'], tags=linha['tag'])

            return jsonify(datetime= datetime.now(),
                        message= 'Importação finalizada com sucesso.',
                        status=200)
            
    except FileNotFoundError:
        return jsonify(datetime= datetime.now(),
                       error= 'Arquivo não encontrado.',
                       status=404)
