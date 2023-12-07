from ting_file_management.queue import Queue


def word_searcher(data, word: str, content: bool):
    result = []

    for item in list(data):
        file_info = item["nome_do_arquivo"]
        lines = item["linhas_do_arquivo"]
        occurrences = word_verifier(lines, word, content)

        if occurrences:
            to_return = {
                "palavra": word,
                "arquivo": file_info,
                "ocorrencias": occurrences,
            }
            result.append(to_return)

    return result


def word_verifier(lines, word, content):
    occurrences = []

    for i, line in enumerate(lines, start=1):
        if word in line.lower():
            if content:
                occurrences.append({"linha": i, "conteudo": line})
            else:
                occurrences.append({"linha": i})

    return occurrences


def exists_word(word: str, instance: Queue):
    lower_word = word.lower()
    return word_searcher(instance._data, lower_word, False)


def search_by_word(word, instance):
    lower_word = word.lower()
    return word_searcher(instance._data, lower_word, True)
