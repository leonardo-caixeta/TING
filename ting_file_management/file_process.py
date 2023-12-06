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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


queue = Queue()

process('statics/arquivo_teste.txt', queue)
print(1)
process('statics/arquivo_teste.txt', queue)
print(2)
print(queue)
