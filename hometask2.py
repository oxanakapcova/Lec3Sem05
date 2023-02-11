# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе
# лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# ИГРА ДВУХ ИГРОКОВ
import random
# 1 часть, представление игроков и жеребьевка
gamer_first = input('Первый игрок ведите ваше имя:')
gamer_second = input('Второй игрок введите ваше имя: ')
gamers = []
step = random.randint(1, 2) # определяем кто ходит первый, игрок 1 или игрок 2
# print(f'Результат жребьевки: первым ходит игрок {step}')
sweets_amount_gamer = None
sweets_amount_full = 2021
if step == 1:
    print(f'По результату жребьевки первый ходит игрок {gamer_first}')
    gamers = [gamer_first, gamer_second]
else:
    print(f'По результату жребьевки первый ходит игрок {gamer_second}')
    gamers = [gamer_second, gamer_first] # чтобы первым ходил именно второй игрок
# 2 часть
is_winner = False
winner_name = None
while not is_winner:
        for gamer in gamers:
            print(f'Ход пользователя {gamer}.')
            sweets_amount_gamer = int(input('введите количество конфет от 1 до 28 включительно: '))
            if sweets_amount_gamer > 28 or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                while sweets_amount_gamer > 28 or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                    print('Число конфет должно быть от 1 до 28 включительно и не превышать остаток')
                    sweets_amount_gamer = int(input('введите количество конфет от 1 до 28 включительно: '))
            sweets_amount_full -= sweets_amount_gamer
            print(f'Осталось {sweets_amount_full} конфет')
            if sweets_amount_full == 0: # условие победы - не осталось конфет
                is_winner = True
                winner_name = gamer
                print(f'Победитель {gamer}')
                break




