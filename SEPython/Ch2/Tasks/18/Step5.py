text = input()

border = "+" + "-" * 29 + "+"
print(border)
print("| {:^27s} |".format(text))
print(border)