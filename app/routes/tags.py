from app import app

from flask import request

from app.services.db_delete import delete_tag
from app.services.db_insert import create_tag
from app.services.db_read import read_tag, read_tag_all


@app.route('/add-tag/<tags>', methods=['POST'])
def add_tag(tags: str):

    mensagem = []

    if read_tag(tags) is None:
        create_tag(tags)
        mensagem.append({"mensagem": f'A tag {tags} foi adicionada com sucesso.'})

    else:
        mensagem.append({"mensagem": f'A tag {tags} já existe.'})

    return mensagem


@app.route('/tag', defaults={"tag": None})
@app.route('/tag/<tag>')
def tag(tag):

    if tag is None:
        return [i['tag'] for i in read_tag_all()]

    for i in tag.split(";"):
        if read_tag(i) is None:
            return {"mensagem": f'A tag {i} não foi encontrada no banco de dados.'}

        return {"mensagem": f'A tag {i} existe.'}

    
@app.route('/del-tag/<tag>', methods=['DELETE'])
def del_tag(tag):

    if delete_tag(tag) is None:
        return {"error": f'A tag {tag} não foi encontrado em nosso banco de dados.'}

    return {"mensagem": f'A tag {tag} foi excluída.'}