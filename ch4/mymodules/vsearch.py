def search_for_vowels(phrase: str) -> set:
    """ Выводит гласные, найденные во введённой фразе. """
    vowels = set('aeiou')

    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """ Возвращает множество букв из 'letters', найденных в 'phrase' """
    return set(letters).intersection(set(phrase))
