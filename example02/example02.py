# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random

def player_turn(max_amount, total_candy, player): # total_candy - всего конфет
    take_candy = -1
    while take_candy < 0 or take_candy > 28 or take_candy > total_candy:
        take_candy = input(f'Сколько конфет из {total_candy} возьмет игрок {player}?: ')
        if take_candy.isdigit():
            take_candy = int(take_candy)
            if take_candy > 28 or take_candy < 1:
                print('Вы взяли недопустимое количество конфет. Нужно от 1 до 28. Сосредоточьтесь и попробуйте еще раз: ')
                take_candy = -1
            elif take_candy > total_candy:
                print(f'На столе осталось всего {total_candy} конфет. Сколько возьмете?:')
                take_candy = -1
        else:
            print('Вы ввели какую-то ерунду. А нужно просто число от 1 до 28. Сделайте свой выбор:')
            take_candy = -1
    return take_candy

def bot_turn(max_amount, total_candy):
    take_candy = total_candy % 29
    if take_candy == 0:
        take_candy = random.randint(1, 28)
    print(f'Бот берет {take_candy} конфет(у).')
    return take_candy    

candy = 201
max_candy = 28

print('-----------------------------------------------------------------------------------------')
print('На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга.') 
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.') 
print('Все конфеты оппонента достаются сделавшему последний ход.')
print(f'---------------------------------------------------------------------------------------\n')
player_name = []
player_name.append(input('Имя первого игрока: '))
player_name.append(input('Имя второго игрока: '))

turn_player = random.randint(0, 1)

print(f'Первый ход за {player_name[turn_player]}')

while candy > 0:
    if 'bot' not in player_name[turn_player]:
        candy -= player_turn(max_candy, candy, player_name[turn_player])
    else:
        candy -= bot_turn(max_candy, candy)
    print(f'Осталось конфет - {candy}.')
    turn_player = int(not bool(turn_player))
print(f'Победил игрок {player_name[int(not bool(turn_player))]}!')