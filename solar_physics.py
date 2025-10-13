from random import randint

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        else:
            dx = obj.x - body.x
            dy = obj.y - body.y
            r = (dx ** 2 + dy ** 2) ** 0.5

        if r == 0:
            continue

        F = gravitational_constant * body.m * obj.m / r ** 2
        body.Fx += F * dx / r
        body.Fy += F * dy / r

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    ay = body.Fy / body.m

    body.Vx += ax * dt
    body.Vy += ay * dt

    body.x += body.Vx * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)

def calculate_uglovaya_skorost(body, central_body):
    R = ((body.x - central_body.x) ** 2 + (body.y - central_body.y) ** 2) ** 0.5
    if R == 0:
        return 0
    w = (body.Vx ** 2 + body.Vy ** 2) / R
    return w

def vtoroy_zakon_Keplera(body, central_body):
    Rx = body.x - central_body.x
    Ry = body.y - central_body.y
    R = ((body.x - central_body.x) ** 2 + (body.y - central_body.y) ** 2) ** 0.5
    cos_a = (body.Vx * Rx - body.Vy * Ry)/((body.Vx ** 2 + body.Vy ** 2) * R)
    sin_a = (1 - cos_a ** 2) ** 0.5
    v_sector = (body.Vx ** 2 + body.Vy ** 2) * R * sin_a
    return v_sector


if __name__ == "__main__":
    print("This module is not for direct call!")



star = Star()
star.m = 1.989e30
star.x = 0
star.y = 0

planet = Planet()
planet.m = 5.972e24
planet.x = 1.496e11
planet.y = 0
planet.Vx = 0
planet.Vy = 29780

space_objects = [planet]

dt = 3600
central_body = star

mas = []
for i in range(len(space_objects)):
    mas.append([0] * dt)
delta = [0] * len(space_objects)
for t in range(dt):
    for i in range(len(space_objects)):
            mas[i][t] = vtoroy_zakon_Keplera(space_objects[i], central_body)
    recalculate_space_objects_positions(space_objects, t)
for j in range(len(space_objects)):
    sr = sum(mas[j])/dt
    delta[j] = max(sr - min(mas[j]), max(mas[j]) - sr)

print(delta)

