from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        str_items = ""
        for i in range(len(self._data)):
            value = self._data[i]
            str_items += str(value)
            if i + 1 < len(self._data):
                str_items += ", "

        return "Queue(" + str_items + ")"

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index: int):
        if index < 0 or index >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
