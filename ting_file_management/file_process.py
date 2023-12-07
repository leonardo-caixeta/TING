from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    for i in instance._data:
        if i['nome_do_arquivo'] == path_file:
            return None

    read_file = txt_importer(path_file)
    new_item = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(read_file),
        'linhas_do_arquivo': read_file
    }
    instance.enqueue(new_item)
    print(new_item, file=sys.stdout)


def remove(instance: Queue):
    if not len(instance):
        return print("Não há elementos", file=sys.stdout)

    removed_item = instance.dequeue()['nome_do_arquivo']
    print(f"Arquivo {removed_item} removido com sucesso", file=sys.stdout)


def file_metadata(instance: Queue, position):
    try:
        item_from_position = instance.search(position)
        return print(item_from_position, file=sys.stdout)

    except IndexError:
        print("Posição inválida", file=sys.stderr)
