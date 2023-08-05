import simple_draw as sd

sd.resolution = (1200, 600)

#Нарисовать закрашенный пузырёк
point = sd.get_point(300, 300)
sd.circle(center_position = point, radius = 50, color = (255, 255, 0), width = 0)
sd.sleep(1)
sd.clear_screen()

#Нарисовать пузырёк - три вложенных окружности с шагом 5 пикселей
point = sd.get_point(300, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position = point, radius = radius, width = 3)
sd.sleep(1)
sd.clear_screen()

#Написать функцию рисования пузырька, принимающую 3 (или более) аргумента: точка рисования, шаг и цвет
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += 5
        sd.circle(center_position = point, radius = radius, width = 3, color = color)
sd.sleep(1)
sd.clear_screen()

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    bubble(point = point, step = 5, color = sd.COLOR_GREEN)
sd.sleep(1)
sd.clear_screen()

#Нарисовать четыре ряда по 10 пузырьков
for y in range(100, 401, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point = point, step = 5, color = sd.COLOR_GREEN)
sd.sleep(1)
sd.clear_screen()

#Нарисовать 100 случайно расположенных пузырьков случайного цвета
for _ in range(100):
    point = sd.random_point()
    bubble(point = point, step = 5, color = sd.random_color())
sd.sleep(1)
sd.clear_screen()
