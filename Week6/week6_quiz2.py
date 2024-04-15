month = int(input("월을 입력하시오 : "))
day = 0

if month in [1, 3, 5, 7, 8, 10, 12]:
    day = 31
elif month in [4, 6, 9, 11]:
    day = 30
elif month == 2:
    day = 28

print("월의 날수는 %d일 입니다." % day)