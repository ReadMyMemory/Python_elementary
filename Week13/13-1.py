alist = []
average, sum = 0, 0
print("====================================")
for _ in range(5):
    temp = int(input("정수를 입력하시오: "))
    alist.append(temp)
    sum += temp

print("평균 = %.1f" % (sum / 5))
