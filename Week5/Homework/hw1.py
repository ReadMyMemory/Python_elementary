a = int(input("첫 번째 숫자를 입력하시오 : "))
b = int(input("두 번째 숫자를 입력하시오 : "))
c = int(input("세 번째 숫자를 입력하시오 : "))

#조건문을 활용하라고 했기 때문에 해당 코드는 사용하지 않는다.
# print("가장 큰 숫자는"+ str(max(a, b, c)) + "입니다.")

max = 0 # 최댓값 저장하는 변수

if a > b:
    if c > a:
        max = c
    else:
        max = a
else:
    if c > b:
        max = c
    else:
        max = b

print("가장 큰 숫자는 " + str(max) + " 입니다.")