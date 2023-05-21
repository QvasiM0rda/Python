chapter = input() + ' '
page = ' ' + input()
dots = 40 - len(chapter)
print(chapter + page.rjust(dots, '.'))