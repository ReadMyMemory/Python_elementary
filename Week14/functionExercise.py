# 1차시 수업은 못들음
# 함수 관련 예제 적기

def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

print(get_sum(1, 10))
