i, k = 0, 0

for i in range(2, 10, 1):
    print("## %d단 ##" % i)  # Code06-07.py에서 이 부분을 추가. 각 단의 제목이 출력되도록
    for k in range(1, 10, 1):
        print("%d X %d = %2d" % (i, k, i * k))
    print("")