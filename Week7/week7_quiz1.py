alist = []
sum = 0

temp = int(input("숫자 1, 입력하시오: "))
alist.append(temp)
sum += temp
temp = int(input("숫자 2, 입력하시오: "))
alist.append(temp)
sum += temp
temp = int(input("숫자 3, 입력하시오: "))
alist.append(temp)
sum += temp
temp = int(input("숫자 4, 입력하시오: "))
alist.append(temp)
sum += temp
temp = int(input("숫자 5, 입력하시오: "))
alist.append(temp)
sum += temp

print("입력값은", alist)
print("입력 숫자의 합은", sum)
