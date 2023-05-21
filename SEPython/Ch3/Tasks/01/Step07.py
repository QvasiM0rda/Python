#filename = input()
filename = "index-2.html"

file = open(filename, encoding="utf-8")
html = file.read()
header = html[html.find("<h1>") + 4:html.find("</h1>")]
html = html.replace(header, header.strip().upper(), 1)
print(html)