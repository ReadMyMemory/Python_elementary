import turtle as tu

t = tu.Turtle()
t.shape("turtle")
t.penup() #펜을 올려서 그림이 그려지지 않게 한다."
t.goto(100, 100) #거북이를 (100, 100)으로 이동시킨다
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100,-100)
t.write("거북이가 여기로 오면 음수입니다.")
t.goto(0, 0)
t.pendown()
s = tu.textinput("", "숫자를 입력하시오:")
n = int(s)
if n > 0:
    t.color("red")
    t.goto(100, 100)
if n == 0:
    t.color("yellow")
    t.goto(100, 0)
if n < 0:
    t.color("blue")
    t.goto(100, -100)
tu.done()

