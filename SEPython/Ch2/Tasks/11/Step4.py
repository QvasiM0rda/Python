text = input()
first_h1_position = text.find("<h1>") + 4
last_h1_position = text.rfind("</h1>")
print(text[first_h1_position:last_h1_position])
