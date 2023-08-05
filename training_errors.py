while True:
    try:
        numb = int(input('Введите число, для выхода введите 100: '))
        if numb == 100:
            break
        result = 100/numb
        print(result)
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
    except:
        print('Что-то пошло не так!')
