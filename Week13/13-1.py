alist = []  # 공백 리스트 생성
average, sum = 0, 0
print("====================================")
for _ in range(5):
    temp = int(input("정수를 입력하시오: "))
    alist.append(temp)
    sum += temp

# 리스트의 크기를 확인하는 len()함수를 이용하라고 하였으므로 해당 라인에서 사용.
print("평균 = %.1f" % (sum / len(alist)))
