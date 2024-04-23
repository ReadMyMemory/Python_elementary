import turtle
import random

## 함수 선언 부분 ##
def screenRightClick(x, y) :
    global r, g, b, tSize, tAngle
    r = random.random()
    g = random.random()
    b = random.random()
    tSize = random.randrange(1, 10)
    tAngle = random.randrange(1, 360)
    turtle.color(r, g, b)
    turtle.pencolor(r, g, b)
    turtle.pendown()
    turtle.goto(x, y)
    #클릭한 위치까지 이동한 후 랜덤한 크기, 각도의 거북이 도장이 찍히도록 하랬으므로.
    turtle.shapesize(tSize)
    turtle.right(tAngle)
    turtle.stamp()

## 변수 선언 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.onscreenclick(screenRightClick, 3)

turtle.done()