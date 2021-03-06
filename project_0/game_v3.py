"""Игра угадай число
компьютер сам угадывает
количество попыток не должно превышать 20
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0 #число попыток
    min = 0 #начальное минимальное значение загаданного числа
    max = 100 #начальное максимальное значение загаданного числа

    while True:
        count += 1
        predict_number = round((min+max)/2) # «складываем вдвое» область поиска, пока не останется одно число
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number > predict_number:
            min = predict_number
        elif number < predict_number:
            max = predict_number
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)