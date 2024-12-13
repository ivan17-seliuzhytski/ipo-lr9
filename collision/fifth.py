class RectCorrectError(Exception):
    pass
def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0
    for rect in rectangles:
        (x1, y1), (x2, y2) = rect
        if (x1 >= x2 or y1 >= y2):
            raise RectCorrectError(f"Некорректный прямоугольник: {rect}")
    first = rectangles[0]
    for rect in rectangles[1:]:
        (x1, y1), (x2, y2) = first
        (x3, y3), (x4, y4) = rect
        left=max(x1,x3)
        bottom = max(y1, y3) 
        right = min(x2, x4) 
        top = min(y2, y4)
        width=right-left
        height=top-bottom
        if (left<right and bottom<top):
            width=right-left
            height=top-bottom
        else:
            return 0
    return width*height