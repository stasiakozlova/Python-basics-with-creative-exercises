def calculation(a, b, operation):
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            result = 'ошибка! Делить на ноль нельзя!'
        else:
            result = a / b
    return result

while True:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    operation = input('Введите операцию (+ - * /): ')
    result = calculation(a, b, operation)
    print(a, operation, b, '=', result)
    question = input('Хотите продолжить? ')
    if question == 'нет':
        break
