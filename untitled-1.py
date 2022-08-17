from random import *
print('Добро пожаловать в числовую угадайку!')

def is_valid(num, num2):
    if num.isdigit and 1 <= int(num) <= num2:
        return True
    else:
        return False
  
def start_game():
    print('')
    r_border = int(input('Выберем диапозон значений для игры от 1 до '))
    digit = randint(1, r_border)
    counter = 0
    while True:
        counter += 1
        print('')
        n = input('Введите число в диапозоне от 1 до {0}: '.format(r_border))
        if is_valid(n, r_border) != True:
            print('А может быть все таки введем число от 1 до {0}?'.format(r_border))
        n_num = int(n)
        if n_num < digit:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n_num > digit:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('')
            print('Вы угадали, поздравляем! Число попыток:', counter)
            print('')
            print('Спасибо, что играли в числовую угадайку.')
            print('')
            print('Я думаю, если постараться, можно улучшить результат, попробуем?')
            break
    return contin_game()

def contin_game():
    text = input('Ответь просто: да \ нет?: ')
    if text.lower() == 'да':
        print('Отлично, поехали!!!')
        return start_game()
    if text.lower() == 'нет':
        print('Грустно, если передумаешь, Я буду тут...')
        return
    else:
        print('Разве так сложно "правильно" ответить? Попробуй еще раз?')
        contin_game()
        
start_game()
