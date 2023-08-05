def decision(ticket):
    part1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    part2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if part1 == part2:
        result = 'У Вас счастливый билет!'
    else:
        result = 'У Вас обычный билет.'
    return result

while True:
    ticket = input('Введите номер Вашего билета: ')
    result = decision(ticket)
    print(result)
    question = input('Хотите продолжить? ')
    if question == 'нет':
        break
