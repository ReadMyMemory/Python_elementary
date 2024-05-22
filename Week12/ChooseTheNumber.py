
print("1부터 100 사이의 숫자를 맞추시오")
attempt = 0
standard = 35

while True:
    temp = int(input("숫자를 입력하시오 "))
    attempt += 1
    if standard > temp:
        print("낮음")
    elif standard < temp:
        print("높음")
    else:
        print("축하합니다. 시도횟수 = %d" % attempt)