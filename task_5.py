import turtle as tl


def fractal(size):
    # for i in range(6):
    # tl.forward(size)
    # tl.right(60)
    if size <= 20:
        return ()
    else:
        for i in range(6):
            tl.left(180)
            fractal(size/2)
            tl.right(120)
            tl.forward(size)
        size = size / 2


size = 150

tl.delay(0.5)  # уменьшение задержки для скорости
tl.penup()
tl.color('red')
tl.goto(-size, 0)
tl.setheading(60)
tl.pendown()

fractal(size)
tl.done()
