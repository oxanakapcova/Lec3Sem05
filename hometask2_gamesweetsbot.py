# игрок против компьютера (без интеллекта)
import random
# 1 часть, представление игрока и жеребьевка
gamer = input('Введите ваше имя:')
bot = 'Бот'
step = random.randint(1, 2)  # определяем кто ходит первый, игрок 1 или бот
sweets_amount_gamer = 0
sweets_amount_full = 121 #2021 число уменьшила для простоты проверки
gamers = []
if step == 1:
    print(f'По результатам жеребьевки первый ходит игрок {gamer}')
    gamers = [gamer, bot]
else:
    print('По результатам жеребьевки первый ходит бот')
    gamers = [bot, gamer]
# 2 часть
is_winner = False
winner_name = None
while sweets_amount_full != 0:
    for player in gamers:
        print(f'Ходит {player}.')
        if player == gamer:
            sweets_amount_gamer = int(input('введите количество конфет от 1 до 28 включительно: '))
            if sweets_amount_gamer > 28 or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                while sweets_amount_gamer > 28 or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                    print('Число конфет должно быть от 1 до 28 включительно и не превышать остаток')
                    sweets_amount_gamer = int(input('введите количество конфет от 1 до 28 включительно: '))
            sweets_amount_full -= sweets_amount_gamer
            print(f'Осталось {sweets_amount_full} конфет')
        else:
            if sweets_amount_full <= sweets_amount_gamer:
                print(f' Бот забирает все {sweets_amount_full} конфет(ы)')
                sweets_amount_full = 0
            else:
                bot_amount = random.randint(1, 28)
                print(f'Бот берет  {bot_amount} конфет(ы)')
                sweets_amount_full -= bot_amount
                print(f'Осталось {sweets_amount_full} конфет(ы)')
        if sweets_amount_full == 0:  # условие победы - не осталось конфет
            print(f'Победитель {player}')
            break
