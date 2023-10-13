from datetime import date, datetime


class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code
        self.country_formats = {
            "ru": "%d.%m.%Y",
            "us": "%m-%d-%Y",
            "ca": "%Y-%m-%d",
            "br": "%d/%m/%Y",
            "fr": "%d.%m.%Y",
            "pt": "%d-%m-%Y",
            }


    def __call__(self, d):
        return datetime.strftime(d, self.country_formats[self.country_code])


ru_format = DateFormatter('ru')

print(ru_format(date(2022, 11, 7)))

us_format = DateFormatter('us')

print(us_format(date(2022, 11, 7)))

ca_format = DateFormatter('ca')

print(ca_format(date(2022, 11, 7)))
