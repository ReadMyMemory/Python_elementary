import turtle as tu

t = tu.Turtle()
t.shape("turtle")


def square(x, y, length):
    t.up()
    t.goto(x, y)
    t.down()
    #t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.left(90)
        #t.end_fill()


square(-200, 0, 100, "red")
square(0, 0, 100)
square(200, 0, 100)

turtle.done()