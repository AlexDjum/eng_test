import random

name = input('Введите ваше имя\n')
score = 0
all_result = []


def testing(txt):
    '''
    Тестирование на словах из документа с перемешанными буквами.
    '''
    with open(txt, encoding='utf-8') as file:
        points = 0
        # Счётчик очков за правильные ответы
        for word in file:
            word = word.strip()
            # Удаление переноса
            word_list = list(word)
            # Преобразование слова в список
            random.shuffle(word_list)
            # Перемешивание букв в слове
            print(f"Угадай слово: {''.join(word_list)}")
            # Вывод слова с перемешанными буквами

            answer = input()
            if answer == word:
                points += 10
                print('Верно! Вы получаете 10 очков.')
                # Если ответ верный + очки
            else:
                print(f'Неверно. Праивльный ответ: {word}.')
                continue

        print(f'Вы набрали {points} очков.\n')
        return points


def write_history(name, total):
    '''
    Запись результатов в документ history.txt
    '''
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name}:{total}\n')


def games_count():
    '''
    Подсчёт сыгранных игр
    '''
    with open('history.txt', encoding='utf-8') as file:
        game_count = 1
        for game in file:
            game_count += 1
        return game_count


def high_score():
    '''
    Вывод таблицы результатов
    '''
    with open('history.txt', 'r', encoding='utf-8') as file:
        history = file.read()
        print(history)


def result():
    '''
    Добавление в пустой список всех результатов
    '''
    with open('history.txt', 'r', encoding='utf-8') as file:
        for items in file:
            names, coins = items.strip().split(':')
            all_result.append(int(coins))


game_count = games_count()
# Вызов счётчика сыгранных игр

points = testing('words.txt')
# Вызов функции тестирования

write_history(name, points)
# Вызов функции для записи результатов

high_score()
# Вывзов функции для вывода таблицы результатов

result()
# Вызов функции для создания списка с очками


print(f'Всего сыграно игр: {game_count}')
print(f'Лучший результат: {max(all_result)}')
