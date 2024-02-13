import json
while True:
    print(f'Привет это телефонный сравочник... сейчас расскажу, что можно тут делать...')
    print(f'Для того, чтобы вывести записи справочника введите 1')
    print(f'Для того, чтобы добавить новую запись введите 2')
    print(f'Для того, чтобы отредактировать существующую запись введите 3')
    print(f'Для того, чтобы найти запись введите 4')
    print(f'Для того, чтобы выйти введите стоп')
    s = input()
    if s == 'стоп':
        break
    elif s == '1':
        with open('my_num.json', 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                for i in data:
                    print(i["firstName"], i["organization"],
                          i["telephon_num"], i["telephon_num_pesonal"])
                print(f'Программа вывела все значения справочника')
            except:
                print('Пустой справочник')
        s = input(f'Продолжим Да? Нет? :')
        if s == 'Да':
            continue
        else:
            break
    elif s == '2':
        with open('my_num.json', 'r+', encoding='utf-8') as file:
            try:
                file.seek(0)
                file_data = json.load(file)

                data = {
                    "firstName": input(f'Введите ФИО: '),
                    "organization": input(f'Введите организацию: '),
                    "telephon_num": input(f'Введите рабочий телефон: '),
                    "telephon_num_pesonal": input(f'Введите личный телефон: ')}

                file_data.append(data)
                file.seek(0)
                json.dump(file_data, file)
            except:
                data = [{
                    "firstName": input(f'Введите ФИО: '),
                    "organization": input(f'Введите организацию: '),
                    "telephon_num": input(f'Введите рабочий телефон: '),
                    "telephon_num_pesonal": input(f'Введите личный телефон: ')}]

                json.dump(data, file)

        print(f'Запись сохранена')
        s = input(f'Продолжим Да? Нет?: ')
        if s == 'Да':
            continue
        else:
            break
    elif s == '3':
        print('Вы попали в раздел редактирования записей')
        print(
            'Для начала найдем запись, которую хотим отредактировать, для этого введите ФИО')
        value = input()
        with open('my_num.json', 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                for i in range(len(data)):
                    if data[i]["firstName"] == value:
                        name = i
                        break
                else:
                    print('Запись не найдена')
                    continue

            except:
                print('Пустой справочник или запись найдена')
        print('Что вы хотите изменить?')
        print('Если вы хотите изменить ФИО нажмите 1')
        print('Если вы хотите изменить организацию нажмите 2')
        print('Если вы хотите изменить рабочий телефон нажмите 3')
        print('Если вы хотите изменить рабочий телефон нажмите 4')
        s = input()
        if s == '1':
            with open('my_num.json', 'r+', encoding='utf-8') as file:
                file_data = json.load(file)

                data[name]["firstName"] = input(
                    f'Введите новое значение ФИО: ')
                file.seek(0)
                json.dump(data, file)
                file.truncate()
        elif s == '2':
            with open('my_num.json', 'r+', encoding='utf-8') as file:
                file_data = json.load(file)

                data[name]["organization"] = input(
                    f'Введите новое значение организации: ')
                file.seek(0)
                json.dump(data, file)
                file.truncate()
        elif s == '3':
            with open('my_num.json', 'r+', encoding='utf-8') as file:
                file_data = json.load(file)

                data[name]["telephon_num"] = input(
                    f'Введите новое значение номера рабочего телефона : ')
                file.seek(0)
                json.dump(data, file)
                file.truncate()
        elif s == '4':
            with open('my_num.json', 'r+', encoding='utf-8') as file:
                file_data = json.load(file)

                data[name]["telephon_num_pesonal"] = input(
                    f'Введите новое значение номера личного телефона: ')
                file.seek(0)
                json.dump(data, file)
                file.truncate()

        print(f'Запись сохранена')

        s = input(f'Продолжим Да? Нет? :')
        if s == 'Да':
            continue
        else:
            break
    elif s == '4':
        print('Вы попали в поиск по сравочнику')
        print('Если ищем по ФИО нажмите 1')
        print('Если ищем по организации нажмите 2')
        print('Если ищем по рабочему телефону нажмите 3')
        print('Если ищем по личному телефону нажмите 4')
        s = input()
        if s == '1':
            print('Введите ФИО')
            value = input()
            with open('my_num.json', 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    flag = False
                    for i in data:
                        if i["firstName"] == value:
                            print(i["firstName"], i["organization"],
                                  i["telephon_num"], i["telephon_num_pesonal"])
                            flag = True
                    if flag == False:
                        print('Запись не найдена')

                except:
                    print('Пустой справочник или запись найдена')
            s = input(f'Продолжим Да? Нет? :')
            if s == 'Да':
                continue
            else:
                break
        elif s == '2':
            print('Введите название организации')
            value = input()
            with open('my_num.json', 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    for i in data:
                        flag = False
                        if i["organization"] == value:
                            print(i["firstName"], i["organization"],
                                  i["telephon_num"], i["telephon_num_pesonal"])
                            flag = True
                    if flag == False:
                        print('Запись не найдена')

                except:
                    print('Пустой справочник или запись найдена')
            s = input(f'Продолжим Да? Нет? :')
            if s == 'Да':
                continue
            else:
                break
        elif s == '3':
            print('Введите рабочий номер телефона')
            value = input()
            with open('my_num.json', 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    flag = False
                    for i in data:
                        if i["telephon_num"] == value:
                            print(i["firstName"], i["organization"],
                                  i["telephon_num"], i["telephon_num_pesonal"])
                            flag = True
                    if flag == False:
                        print('Запись не найдена')

                except:
                    print('Пустой справочник или запись найдена')
            s = input(f'Продолжим Да? Нет? :')
            if s == 'Да':
                continue
            else:
                break
        elif s == '4':
            print('Введите личный номер телефона')
            value = input()
            with open('my_num.json', 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    flag = False
                    for i in data:
                        if i["telephon_num_pesonal"] == value:
                            print(i["firstName"], i["organization"],
                                  i["telephon_num"], i["telephon_num_pesonal"])
                            flag = True
                    if flag == False:
                        print('Запись не найдена')

                except:
                    print('Пустой справочник или запись найдена')
            s = input(f'Продолжим Да? Нет? :')
            if s == 'Да':
                continue
            else:
                break
        else:
            print('Ввели неверные данные идем в начало')
            continue

    else:
        print('Ввели неверные данные ВЫХОД')
        break
