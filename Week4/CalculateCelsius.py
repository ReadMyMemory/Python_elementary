#교재 문제, 화씨 온도 받아서 섭씨온도로 바꾸기

celsius, fahrenheit = 0,0

fahrenheit = int(input("화씨 온도 : "))
celsius = (fahrenheit - 32) * 5 / 9
print("섭씨 온도 : %f" % celsius) # %d를 하면 정수형, %f하면 실수형1
