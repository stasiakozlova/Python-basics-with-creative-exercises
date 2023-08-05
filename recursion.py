# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования сделать 30 градусов (первый плюс 30, второй минус 30).

import simple_draw as sd

sd.resolution = (1200, 600)

def draw_branches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point = start_point, angle = angle + 30, length = length, width = 1)
    v1.draw()
    #sd.sleep(0.1)
    v2 = sd.get_vector(start_point = start_point, angle = angle - 30, length = length, width = 1)
    v2.draw()
    #sd.sleep(0.1)
    point_1 = v1.end_point
    point_2 = v2.end_point
    angle_1 = angle + 30
    angle_2 = angle - 30
    length = length * .75
    draw_branches(start_point = point_1, angle = angle_1, length = length)
    draw_branches(start_point = point_2, angle = angle_2, length = length)

start_point = sd.get_point(600, 30)
draw_branches(start_point = start_point, angle = 90, length = 100)


# 2) Сделать draw_branches рекурсивной
# - в начало функции добавить проверку на длину ветвей, если длина меньше 10, то return 
# - после рисования двух ветвей из первой части добавть
#   вызов самой себя 2 раза из точек-концов нарисованных ветвей
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви.
#   Напомню, концы вечтвей ищустя с помощью .end_point


# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

sd.sleep(3)
sd.clear_screen()

def draw_branches_rand(start_point, angle, length):
    if length < 5:
        return
    v1 = sd.get_vector(start_point = start_point, angle = angle, length = length, width = 1)
    v1.draw()
    #sd.sleep(0.1)
    v2 = sd.get_vector(start_point = start_point, angle = angle, length = length * sd.random_number(80, 120) / 100, width = 1)
    v2.draw()
    #sd.sleep(0.1)
    point_1 = v1.end_point
    point_2 = v2.end_point
    angle_1 = angle + sd.random_number(20, 40)
    angle_2 = angle - sd.random_number(20, 40)
    length1 = length * sd.random_number(70, 80) / 100
    length2 = length * sd.random_number(70, 80) / 100
    draw_branches_rand(start_point = point_1, angle = angle_1, length = length1)
    draw_branches_rand(start_point = point_2, angle = angle_2, length = length2)

start_point = sd.get_point(600, 30)
draw_branches_rand(start_point = start_point, angle = 90, length = 100)

# 4) Дополнительное задание для желающих потренироваться.
# Попробуйте поиграть длиной веток и углами отклонения.
# Например, можно делать длину веток случайной в указанном диапазоне, и угол тоже.
# Для этого пригодится примерно такое:  sd.random_number(30, 40)
# (пример случайного числа от 30 до 40).
