text = input()
new_text = input()

first_h1_position = text.find("<h1>") + 4
last_h1_position = text.rfind("</h1>")
text = text[:first_h1_position] + new_text + text[last_h1_position:]
print(text)