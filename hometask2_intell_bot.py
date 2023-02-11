# наделяем бота интелектом. Чтобы выиграть надо знать остаток от деления и всегда
# потом брать нужное число взависимости от числа игрока
# можно предоставить выбор общего количества конфет и максимального за раз.
import random
gamer = input('Введите ваше имя: ')
bot = 'Бот'
step = random.randint(1, 2)  # определяем кто ходит первый, игрок 1 или бот
sweets_amount_gamer = None
sweets_amount_full = int(input('Введите общее количество конфет: '))
sweets_amount_max = int(input('Введите максимальное количество конфет которое можно взять за 1 раз: '))
gamers = [gamer, bot] # для удобства в цикле
# is_winner = False
# winner_name = None
if step == 1:
    print(f'По результатам жеребьевки первый ходит игрок {gamer}')
# если первым ходит игрок и он знает логику выигрыша, у бота нет шансов, если же игрок логику не знает
# то можно попытаться. Первый ход я вывела вне цикла, бот попытается перехватить инициативу
    sweets_amount_gamer = int(input(f'Введите количество конфет от 1 до {sweets_amount_max} '))
    if sweets_amount_gamer > sweets_amount_max or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
        while sweets_amount_gamer > sweets_amount_max or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
            print(f'Число конфет должно быть от 1 до {sweets_amount_max} включительно и не превышать остаток')
            sweets_amount_gamer = int(input(f'введите количество конфет от 1 до {sweets_amount_max} включительно: '))
    balance = (sweets_amount_full % (sweets_amount_max + 1)) - sweets_amount_gamer
    sweets_amount_full -= sweets_amount_gamer
    print(f'Осталось {sweets_amount_full} конфет')
    if balance > 0: # бот выиграет
        print(f'Ход бота и он берет {balance} конфет(ы)')
        sweets_amount_full -= balance
        print(f'Осталось {sweets_amount_full} конфет(ы)')
        while sweets_amount_full != 0:
            for player in gamers:
                print(f'Ходит {player}.')
                if player == gamer:
                    sweets_amount_gamer = int(input(f'Введите количество конфет от 1 до {sweets_amount_max} '))
                    if sweets_amount_gamer > sweets_amount_max or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                        while sweets_amount_gamer > sweets_amount_max or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                            print(f'Число конфет должно быть от 1 до {sweets_amount_max} включительно и не превышать остаток')
                            sweets_amount_gamer = int(input(f'введите количество конфет от 1 до {sweets_amount_max} включительно: '))
                    sweets_amount_full -= sweets_amount_gamer
                    print(f'Осталось {sweets_amount_full} конфет')
                else:
                    if sweets_amount_full > sweets_amount_max:
                        sweets_amount_gamer = sweets_amount_max - sweets_amount_gamer + 1
                        print(f'Бот берет {sweets_amount_gamer} конфет(ы)')
                        sweets_amount_full -= sweets_amount_gamer
                        print(f'Осталось {sweets_amount_full} конфет')
                    else:  # когда количество будет равно или меньше тому что можно взять за 1 раз их должен забрать бот
                        print(f'Забираю последние {sweets_amount_full} конфет(ы)')
                        sweets_amount_gamer = sweets_amount_full
                        sweets_amount_full -= sweets_amount_gamer  # 0
            if sweets_amount_full == 0:  # условие победы - не осталось конфет
                is_winner = True
                winner_name = gamer
                print(f'Победитель {player}')
                break
    else:
        # возможно игрок знает логику и шансы у бота к победе только если игрок случайно угадал нужное число
        # оставляем игроку шансы на выигрыш и вводим рандомные числа
        balance = random.randint(1,sweets_amount_max)
        print(f'Ход бота и он берет {balance} конфет(ы)')
        sweets_amount_full -= balance
        print(f'Осталось {sweets_amount_full} конфет(ы)')
        while sweets_amount_full != 0:
            for player in gamers:
                if player == gamer:
                    sweets_amount_gamer = int(input(f'Введите количество конфет от 1 до {sweets_amount_max} '))
                    if sweets_amount_gamer > sweets_amount_max or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                        while sweets_amount_gamer > sweets_amount_max or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                            print(
                                f'Число конфет должно быть от 1 до {sweets_amount_max} включительно и не превышать остаток')
                            sweets_amount_gamer = int(input(f'введите количество конфет от 1 до {sweets_amount_max} включительно: '))
                    sweets_amount_full -= sweets_amount_gamer
                    print(f'Осталось {sweets_amount_full} конфет')
                    if sweets_amount_full == 0:
                        print('ПОЗДРАВЛЯЮ ВЫ ВЫИГРАЛИ')
                        break
                else:
                    if sweets_amount_full <= sweets_amount_max:
                        print(f'Забираю последние {sweets_amount_full} конфет(ы)')
                        print('Победитель бот')
                        break
                    else:
                        sweets_amount_gamer = random.randint(1, sweets_amount_max)
                        print(f'Бот берет {sweets_amount_gamer} конфет(ы)')
                        sweets_amount_full -=sweets_amount_gamer
                        print(f'Осталось {sweets_amount_full} конфет(ы)')
# если первый ход бота, выигрышная комбинация
else:
    print('По результатам жеребьевки первый ходит бот')
    sweets_amount_gamer = sweets_amount_full % (sweets_amount_max + 1)
    print(f'Мой ход {sweets_amount_gamer} конфет')
    sweets_amount_full -= sweets_amount_gamer
    print(f'Осталось {sweets_amount_full} конфет(ы)')
    # если бот начинает первым то вначале он выдает остаток от деления общего количества  на максимальное + 1
    # и потом берет такое количество чтобы в сумме с игроком выйте на макс количество +1
    # в данном случае в конце всегда гарантированно останутся конфеты
    while sweets_amount_full != 0:
        for player in gamers:
            print(f'Ходит {player}.')
            if player == gamer:
                sweets_amount_gamer = int(input(f'Введите количество конфет от 1 до {sweets_amount_max} '))
                if sweets_amount_gamer > sweets_amount_max or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                    while sweets_amount_gamer > sweets_amount_max or sweets_amount_gamer < 1 or sweets_amount_gamer > sweets_amount_full:
                        print(f'Число конфет должно быть от 1 до {sweets_amount_max} включительно и не превышать остаток')
                        sweets_amount_gamer = int(input(f'введите количество конфет от 1 до {sweets_amount_max} включительно: '))
                sweets_amount_full -= sweets_amount_gamer
                print(f'Осталось {sweets_amount_full} конфет')
            else:
                if sweets_amount_full > sweets_amount_max:
                    sweets_amount_gamer = sweets_amount_max - sweets_amount_gamer + 1
                    print(f' Бот берет {sweets_amount_gamer} конфет(ы)')
                    sweets_amount_full -= sweets_amount_gamer
                    print(f'Осталось {sweets_amount_full} конфет')
                else:
# когда количество будет равно или меньше тому что можно взять за 1 раз их должен забрать бот
                    print(f'Забираю последние {sweets_amount_full} конфет(ы)')
                    sweets_amount_gamer = sweets_amount_full
                    sweets_amount_full -= sweets_amount_gamer #0
                    if sweets_amount_full == 0:  # условие победы - не осталось конфет
                        # is_winner = True
                        # winner_name = player
                        print(f'Победитель {player}')

