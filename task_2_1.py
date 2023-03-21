"""По длинам трех отрезков, введенных пользователем, определить
возможность существования треугольника, составленного из этих
отрезков. Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или
равносторонним."""

"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Требуется сравнить каждую сторону с суммой двух других. Если хотя бы в одном случае сторона 
окажется больше или равна сумме двух других, то треугольника с такими сторонами не существует"""


def triangle_start():
    a = int(input("Введите длинну стороны треугольника, а = "))
    b = int(input("Введите длинну стороны треугольника, b = "))
    c = int(input("Введите длинну стороны треугольника, c = "))

    if a + b > c and a + c > b and c + b > a:
        print("Треугольник существует.")
        if a == b and c == a and b == a:
            print("Треугольник равносторонний.")
        elif a == b or c == a or b == c:
            print("Треугольник равнобедренный.")
        elif a != b or c != a or b != c:
            print("Треугольник не равносторонний.")
        exit()  # Выход из программы, после того, как определили какой треугольник.

    else:
        print("Треугольник не существует!")
        print("Введите корректно стороны треугольника:")


while True:  # Перезапуска программы если треугольник не существует (пользователь ввел не корректные данные).

    triangle_start()
