# Напишите программу, удаляющую из текста все слова, содержащие ""abv""

def del_abv(text):
    text_list = list(text.split()) # разбиваем и преобразовываем в список
    for world in text_list: # по всем элементам списка(словам)
        if 'abv' in world:
            text_list.remove(world) # удаляем слово целиком
    return ' '.join(text_list) # возвращаем новый список преобразовав в строку

my_text = 'все слова, содержащие ""abv""'# input('type text: ')
print(del_abv(my_text))

