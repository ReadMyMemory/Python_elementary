# 01. 시작값, 끝값+1, 증가값
# 02. range(0, 101, 1) 0부터 100까지 1씩 증가. 즉 100 - 0 + 1 = 101번
# 03. range(5, -1, -1) 5에서 0까지. -1씩 증가. 5, 4, 3, 2, 1, 0 이라서 -1은 나올 수 없음.
# 04. range(1, 1001, 5) 이렇게 하면 1부터 1000까지 5의 배수 출력 가능
# 05. 9부터 1까지 출력해야하므로, range(9, 0, -1) / 출력부는 (dan, i, dan * i)
# 06. 이중, 삼중 같은 중첩 for 문의 반복횟수는 곱하면 됨. 4 * 3 * 2 = 24번 반복.
# 07. while문의 괄호 안에는 조건식이 들어간다.
# 08. for 반복문을 while 반복문으로 바꾸면 다음과 같음.
"""
hap = 0
n = 1234
while n < 4568:
    if n % 444 = 0:
        hap += n
    n += 1
print(hap)
"""

#09. 코드 작성
hap = 0
for i in range(3333, 10000):
    if i % 1234 != 0:
        continue
    else:
        if hap + i > 100000:
            break
        hap += i
print(hap)



