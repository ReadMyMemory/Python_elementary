# 3차시 학습 활동 SELF-STUDY 7-1
# Code07-03.py에서 입력을 4개가 아닌 10개로, 마지막 합계를 구할 때 for문 대신 while문으로

aa = []
for i in range(0, 10):
    aa.append(0)

for i in range(0, 10):
    aa[i] = int(input(str(i+1) + "번째 숫자 : "))

temp, hap = 0, 0
while temp < 10:
    hap += aa[temp]
    temp += 1

print("합계 ==> %d" % hap)
