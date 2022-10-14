from app import app

from flask import request, jsonify

from datetime import datetime

from app.services.db_delete import delete_tag
from app.services.db_insert import create_tag
from app.services.db_read import read_tag_id, read_tag_all, read_tag


@app.route('/tag', methods=['POST'])
def add_tag():

    tag = request.json["tag"]

    mensagem = []

    if read_tag(tag) is None:
        create_tag(tag)
        mensagem.append({"datetime":datetime.now(),
                         "message":f"A tag '{tag}' foi adicionada com sucesso.",
                         "status":201})

    else:
        mensagem.append({"datetime": datetime.now(),
                         "error":f"A tag '{tag}' já existe.",
                         "status":400})

    return jsonify(mensagem)


@app.route('/tag', defaults={"id": None})
@app.route('/tag/<id>')
def tag(id):

    mensagem = []

    if id is None:
        return jsonify(datetime=datetime.now(),
                       data=read_tag_all(),
                       status=200)

    for i in id.split(";"):
        tag = read_tag_id(i)
        if tag is None:
            mensagem.append({"datetime": datetime.now(),
                             "message":f"A tag '{i}' não foi encontrada no banco de dados.",
                             "status":204})

        else:
            mensagem.append({"datetime": datetime.now(),
                             "data": tag,
                             "status":200})

    return jsonify(mensagem)

    
@app.route('/tag/<int:id>', methods=['DELETE'])
def del_tag(id: int):

    if delete_tag(id) is None:
        return jsonify(datetime= datetime.now(),
                       error= f"A tag com o ID '{id}' não foi encontrado em nosso banco de dados.",
                       status=404)

    return jsonify(datetime= datetime.now(),
                   message= f"A tag com o ID '{id}' foi excluída.",
                   status=200)
