import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
           'Можешь быть в этом уверен', 'Мне кажется - да', 'Вероятнее всего',
           'Хорошие перспективы', 'Знаки говорят - да', 'Да','Пока не ясно, попробуй снова',
           'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет',
           'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет! Я - магический шар и я могу ответить на любой твой вопрос!')
name = input('Как тебя зовут? ')
print('Привет', name)
play_again = 'да'

while play_again.lower() in ['да', 'yes']:
    question = input('Задай свой вопрос: ')
    print(random.choice(answers))
    play_again = input('Ещё вопрос? ')

print('До свидания!')