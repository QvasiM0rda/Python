class SuperString:
    def __init__(self, string):
        self._string = string


    def __str__(self):
        return self._string


    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self._string + other._string)
        return NotImplemented


    def __mul__(self, n):
        if isinstance(n, int):
            return SuperString(self._string * n)
        return NotImplemented


    def __rmul__(self, n):
        return self.__mul__(n)
    

    def __truediv__(self, n):
        if isinstance(n, int):
            return SuperString(self._string[:len(self._string) // n])
        return NotImplemented


    def __lshift__(self, n):
        if isinstance(n, int):
            return SuperString(self._string[:-n] if n else self._string)
        return NotImplemented


    def __rshift__(self, n):
        if isinstance(n, int):
            return SuperString(self._string[n:] if n else self._string)
        return NotImplemented


names = ['Карп', 'Фотий', 'Любосмысл', 'Клавдия', 'Милован', 'Светлана', 'Александра', 'Ираида', 'Трифон', 'Добромысл',
         'Евпраксия', 'Радим', 'Эдуард', 'Аристарх', 'Ульяна', 'Ираклий', 'Юлия', 'Марк', 'Демид', 'Творимир', 'Орест',
         'Феоктист', 'Тимур', 'Филипп', 'Аверьян', 'Эраст', 'Осип', 'Станислав', 'Адриан', 'Милан', 'Парфен', 'Велимир',
         'Филимон', 'Ратибор', 'Элеонора', 'Феофан', 'Ирина', 'Кузьма', 'Панфил', 'Венедикт', 'Парамон', 'Влас',
         'Надежда', 'Фрол', 'Мартьян', 'Моисей', 'Леонид', 'Мариан', 'Марина', 'Филарет', 'Валентина', 'Севастьян',
         'Светозар', 'Родион', 'Ростислав', 'Капитон', 'Герман', 'Геннадий', 'Иосиф', 'Гостомысл', 'Епифан', 'Гордей',
         'Ферапонт', 'Януарий', 'Денис', 'Галина', 'Аггей', 'Харлампий', 'Акулина', 'Климент', 'Автоном', 'Никанор',
         'Фортунат', 'Сила', 'Федосий', 'Виктор', 'Арсений', 'Дементий', 'Спартак', 'Евгений', 'Феликс', 'Ананий',
         'Нинель', 'Стоян', 'Остромир', 'Никифор', 'Клавдий', 'Чеслав', 'Афанасий', 'Наум', 'Рубен', 'Азарий',
         'Виктория', 'Синклитикия', 'Тимофей', 'Фёкла', 'Нонна', 'Ким', 'София']

superstring = SuperString('bee')
print(superstring.__add__([]))
print(superstring.__mul__(()))
print(superstring.__truediv__({}))
print(superstring.__lshift__(set()))
print(superstring.__rshift__('geek'))
