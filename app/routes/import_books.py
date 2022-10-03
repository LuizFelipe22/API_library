from app import app

import csv

from app.services.db_insert import create_book, create_tag
from app.services.db_read import read_book, read_tag


@app.route('/importar-book/<path:filename>', methods=['POST'])
def import_book(filename: str):

    try:
        with open(f'/{filename}', "r") as file:
            file_csv = csv.DictReader(file, delimiter=",")
            
    except FileNotFoundError:
        return {"mensagem": 'Arquivo não encontrado.'}

    for linha in file_csv:

        for tag in linha['tag'].split(";"):
            if read_tag(tag) is None:
                create_tag(tag)

        if read_book(linha['text']) is None:
            create_book(book=linha['text'], type=linha['type'], tags=linha['tag'])

    return {"mensagem": 'Importação finalizada com sucesso.'}
