from collections import Counter


def print_bar_chart(data, mark):
    elements = Counter(data)
    max_len = len(max(elements, key=len))
    for element, amount in sorted(elements.items(), key=lambda elem: elem[1], reverse=True):
        print(f"{element.ljust(max_len)} |{mark * amount}")


print_bar_chart('beegeek', '+')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java', 'Python']
print_bar_chart(languages, '#')
