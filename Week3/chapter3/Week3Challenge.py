import turtle as t

# 터틀 그래픽을 활용하여 사용자에게 사이즈(크기)를 입력받아 도형을 그리시오.
tempSizeValue = float(input("도형을 그리는 프로그램입니다. 해당 프로그램은 원을 그립니다. 사이즈를 입력해주세요 : "))

t.shape('turtle')
t.color('blue')
t.up()

#빨간 원 그리기
t.goto(0, -tempSizeValue)
t.down()
t.color('red')
t.circle(tempSizeValue)
t.up()
t.goto(0, 0)
t.color('blue')

t.done()
