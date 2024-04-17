import turtle as tu

alist = []
alist.append(input("색상 #1을 입력하시오: "))
alist.append(input("색상 #1을 입력하시오: "))
alist.append(input("색상 #1을 입력하시오: "))

t = tu.Turtle()
t.shape("turtle")
t.color("black")

#첫 번째 원
t.pendown()
t.fillcolor(alist[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()

#두 번째 원
t.goto(100, 0)
t.pendown()
t.fillcolor(alist[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()

#세 번째 원
t.goto(200, 0)
t.pendown()
t.fillcolor(alist[2])
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()

tu.done()
