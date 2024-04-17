import random


"""
# 1. 직접 넣기
alist = [1, 2, 3, 4, 5]
print(alist)
"""


"""
# 2. append로 리스트 값 추가하기
alist = []
alist.append('가')
alist.append('나')
alist.append('다')
print(alist)
"""

"""
# 3. input받아서 append로 값 추가
alist = []
s_name = input("수강생의 이름을 입력하세요 : ")
alist.append(s_name)
p_name = input("수강생의 이름을 입력하세요 : ")
alist.append(p_name)
print(alist)
"""

"""
#4. 리스트에서 특정 값이 있으면 print 하는 조건문 사용하기
color = ['red', 'green', 'blue']
print(color)

c = input("컬러(영문)을 입력하세요 : ")
if c in color:
    print("해당 색깔이 존재합니다.")
else:
    print("해당 색깔은 존재하지 않습니다.")
"""

"""
#5. random 함수 사용해서 시간 출력하기

time = random.randint(1, 24)

print("지금 시각은 %d시입니다" % time) # 이렇게 써도 되고
print("지금 시각은 "+str(time)+"시입니다") # 이렇게도 가능하고
print(f"지금 시각은 {time}시입니다") # 이렇게도 가능하다.
"""

"""
#6. 랜덤함수 사용해서 날씨 출력
sunny = random.choice([True, False])

if sunny:
    print("날씨가 화창합니다.")
else:
    print("날씨가 흐립니다.")
"""


