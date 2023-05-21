filename = input()
name = input()

file = open(filename, encoding="utf-8")
template = file.read().replace("{{ name }}", name)
print(template)