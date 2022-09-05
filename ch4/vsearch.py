def search_for_vowels(word:str) -> set:
    """Выводит гласные, найденные во введенном слове."""
    vowels = set('aeiou')
    
    return vowels.intersection(set(word))
