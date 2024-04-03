# if 조건식 배우기

# 1. 큰 거 찾기
a = 1000
if a >= 100:
    print("100보다 큰 숫자입니다.")
# print("변수 값을 확인하세요.")

print("=====================")

# 2. 작은 거 찾기
a = 50
if a >= 100:
    print("100보다 큰 숫자입니다.")
print("변수값을 확인하세요. 100보다 작습니다.")

print("=====================")

# 3. 양수 음수 구별
a = 50
if a >= 0:
    print("양수입니다.")
else:
    print("음수입니다.")
print("종료합니다.")

print("=====================")

# 4. input 값이 짝수인지 홀수인지 계산하기
a = int(input("정수를 입력하세요 : "))
if a % 2 == 0:
    print("짝수를 입력했군요.")
else:
    print("홀수를 입력했네요.")

print("=====================")

# 5. 입력한 숫자를 출력하고, 짝수인지 홀수인지 알려주기.
a = int(input("정수를 입력하세요 : "))
print("입력한 숫자는 >> "+str(a)+" << 입니다")
if a % 2 == 0:
    print("짝수입니다!")
else:
    print("홀수입니다!")

print("=====================")

# 6.나이를 입력받고, 15세 조건에 따라 관람할 수 있는 나이대인지 판별
print("안녕하세요? OOO 영화관입니다.")
a = int(input("나이를 입력하시오 : "))
if a > 15:
    print("이 영화를 보실 수 있습니다.")
else:
    print("이 영화를 보실 수 없습니다.")

print("=====================")

# 7.놀이동산에서 어트렉션을 이용할 수 있는 키와 나이인지 확인
print("안녕하세요? OOO 테마파크입니다.")
a = int(input("나이를 입력하시오 : "))
b = int(input("키를 입력하시오 : "))
if a > 13 and b > 150:
    print("어트렉션 이용 가능.")
else:
    print("어트렉션 이용 조건 미충족")

print("=====================")

# 8.중첩 if문 사용하기
a = 75
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작군요.")
    else:
        print("와~ 100보다 크군요?")
else:
    print("에구~ 50보다 작군요?")

print("=====================")

# 9. 숫자를 입력받고 0, 양수, 음수 판단하기
a = int(input("정수를 입력하세요 : "))
if a>=0:
    if a == 0:
        print("입력한 값은 0이다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")

# 10. random 라이브러리 사용하기
import random
print("주사위 게임을 시작합니다.")
dice = random.randrange(6)+1
print("주사위 값은 "+str(dice)+"입니다.")
print("주사위 게임을 종료합니다.")

# 11. elif 사용하여 학점 계산
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
print("학점입니다.")

# 12. 윤년 계산. 4로 나누어 떨어지면 윤년, 100으로 나누어 떨어지는 건 제외. 400으로 나누어 떨어지는 연도는 윤년이다.
year = int(input("연도를 입력하시오 : "))
if (year % 4 == 0 and 100 != 0) or year % 400 == 0:
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 아닙니다.")