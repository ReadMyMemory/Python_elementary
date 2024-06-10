# for문 작성 방법
# for 변수 in range(시작값, 끝값 + 1, 증가값)
# 증가값은 따로 안쓰면 1이다.

# 변수를 사용하고 싶지 않을 땐 _를 사용한다.
# for _ in range(1, 3)

# range 대신 리스트 써도 된다.
# 예를 들어 range(0,3)는 [0, 1, 2] 과 같다.
"""
for i in [0, 1, 2] :
#   print("반복문 출력 횟수 i번" % i)
# 이렇게 작성 가능
"""

# 구구단 출력, 구구단 역순 출력
# Code06-06.py
i, dan = 0, 0
dan = int(input("단을 입력하세요 : "))

for i in range(1, 10, 1):
    print("%d X %d = %2d" % (dan, i, dan * i))

print("======= 여기부터 구구단 역순 출력 =======")

# SELF-STUDY 6-2
# Code06-06.py에서 구구단 역순 출력
for i in range(9, 0, -1):
    print("%d X %d = %2d" % (dan, i, dan * i))

