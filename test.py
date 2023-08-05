def power_function(number, power):
    print('Функцию вызвали с аргументами ', number, power)
    power_value = number ** power
    return power_value

result = power_function(2, 3)
print(result)
