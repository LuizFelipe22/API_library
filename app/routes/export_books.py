from app import app

from csv import DictWriter

from app.services.db_read import read_book_all


@app.route('/export-book/<path:filename>', methods=['POST'])
def export_book(filename: str):

    try:
        with open(f'/{filename}', 'w') as arquivo:
            writer = DictWriter(arquivo, fieldnames=['Book', 'Tipo', 'Tags']) 
            writer.writeheader() 
            writer.writerows(read_book_all())

    except FileNotFoundError:
        return {"mensagem": 'Arquivo não encontrado.'}

    return {"mensagem": 'Exportação concluída com sucesso.'}

