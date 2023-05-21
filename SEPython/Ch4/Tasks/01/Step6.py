languages = ['Python', 'C++', 'JavaScript', 'Java']
first, second = int(input()), int(input())
languages[first], languages[second] = languages[second], languages[first]
print(languages)
