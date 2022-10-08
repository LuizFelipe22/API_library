from app import app

from datetime import datetime
from csv import DictWriter
import os

from app.services.db_read import read_book_all_export

from flask import jsonify


@app.route('/export-book', methods=['POST'])
def export_book():

    filename = os.path.join(os.environ['HOME'] + '/Downloads')

    with open(f'{filename}/livros {datetime.now()}.csv', 'w+') as arquivo:
        writer = DictWriter(arquivo, fieldnames=['book', 'tipo', 'tags']) 
        writer.writeheader() 
        writer.writerows(read_book_all_export())

    return jsonify(datetime= datetime.now(),
                   message= 'Exportação concluída com sucesso.',
                   status=201)
