# 문자열 함수
# find()와 rfind()
# 왼쪽에서부터 찾냐, 오른쪽부터 찾냐 차이임. 위치 인덱스 반환 기준이 왼쪽 vs 오른쪽인 것.
# index는 find랑 비슷하지만 찾는데 사용하는 문자열 값(ex. index(특정값))이 존재하지 않으면 오류 발생.

# 문자열 공백 삭제하기.
# strip() : 양쪽 다 공백 제거
# rstrip() : 오른쪽 공백만 제거
# lstrip() : 왼쪽 공백만 제거
# 그러면 가운데 공백은 어떻게 빼나요? 라고 질문 할 수 있다.

# 문자열 분리, 결합
# split(), splitlines(), join()
# 기본 split()은 공백을 기준으로 나눈다.
# ss.split() = ['하나', '둘', '셋']
# 특정 문자를 기준으로 나누도록 지정도 가능하다. ss.split(':')
# splitlines는 똑같이 나누는데 행 단위로 나눈다.
# join은 글자 중간에 문자를 넣는다.
# ss = '%', ss.join('파이썬') = 파%이%썬

# 함수명에 대입. map(함수명, 리스트명)
# 리스트 값 하나하나를 함수명에 대입. 즉 매핑
# after = list(int, before))에서 int는 int(값)과 같은 역할

# 문자열 정렬, 채우기
# center, ljust, rjust, zfill

#문자열 구성 파악하기
# .isdigit() 숫자로만 구성되어있니? '1234'라면, 전체를 보는 게 아니라 따옴표 안의 값을 보기 때문에 True임.
# .isalpha() 알파벳으로 구성되어있니?
# .isalnum(), islower(), isupper(), isspace()


#...여기부턴 실습

test = '프로그래밍 기초'
print(test[:5])  # 프로그래밍
print(test * 2)  # 프로그래밍 기초프로그래밍 기초
print(len(test))  # 8

print("==========================")

test = 'hello 파이썬'
print(test.upper())  # HELLO 파이썬, 이때 원본이 바뀌는 것은 아님을 꼭 기억하자!
print(test.title())  # Hello 파이썬, 맨 앞 글자만 대문자
print(test.count('파이썬'))  # 1, 문자열 안에 파이썬은 하나.

print("==========================")

test = '파이썬 '
print(test.strip())  #'파이썬', 공백이 빠져서 나옴
print(test.strip('/'))  #'파이썬 ', 적용 안되는 게 정상 /가 없으니
print(test.lstrip()) #'파이썬 ', 적용 안되는 게 정상 왼쪽 공백 삭제

test = '수요일 프로그래밍 기초'
print(test.split())  # ['수요일',  '프로그래밍', '기초']

print("==========================")

ss = '/'
print(ss.join('이재현')) # 이/재/현

print("==========================")

test = '수요일 프로그래밍 기초'
print(test.center(30)) # 전체길이를 30으로 잡고 중앙 정렬함, 기본은 공백
print(test.center(30, '/')) # 전체길이를 30으로 잡고 중앙 정렬함, 특정 문자로 채울 수 있음

print("==========================")

print('123'.isdigit())  # True, 따옴표 안의 값에서 숫자만 있는지를 파악

print("==========================")
test = '수요일 파이썬'
print(test.replace('수요일', 'Wen')) # Wen 파이썬

print("==========================")

instr, outstr = "", ""
count, i = 0, 0

instr = input("문자열을 입력하시오: ")
count = len(instr)

for i in range(0, count):
    outstr = outstr + instr[count-(i+1)]

print("거꾸로 출력한 문자열 : ==> ")
