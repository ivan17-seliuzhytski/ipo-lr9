def vvod():
    kolvo = int(input("Сколько у вас прямоугорльников: "))
    for i in range(kolvo): 
        print(f"Введите координаты {i + 1} прямоугольника ")
        x1 = int(input("x левого нижнего угла: \n"))
        y1 = int(input("y левого нижнего угла: \n"))
        x2 = int(input("x правого верхнего: \n"))
        y2 = int(input("y правого верхнего: \n"))
        rectangl = ((x1, y1), (x2, y2))
        rectangles.append(rectangl)
from collision import second, third, fourth, fifth
second.isCorrectRect()
third.isCollisionRect() 
fourth.intersectionAreaRect()
rectangles = []
vvod()
fifth.intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {fifth.intersectionAreaMultiRect(rectangles)}")