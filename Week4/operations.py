a=0xFF
b=0o77
c=0b1111

int(10)
int('10')
int('1010', 2) # 뒤에 인자는 몇 진수 값인지 체크 ex) 2 -> 10
int('101010', 2)
int('ff', 16)


#13. 다음표현이 틀린 이유?
#int('1002', 2) # 2이상의 값이 들어가면 안됨
#int('1008', 8) # 8이상이 값이 들어가면 안됨
#int('AAFG', 16) # G는 16진수에서 표현할 수 없는 값임


bin(128) # '0b10000000' 표현을 위해 8비트 필요
oct(50) # 10진수 50을 8진수로 변환 시 '0o62'
hex(255) # 10진수 255를 16진수로 변환 시 '0xff

#15. 실행결과가 나올 수 있도록 코드 작성

#10진수 ===> 12345678
#16진수 ===> 0xbc614e
#8진수 ===> 0o57060516
#2진수 ===> 0b101111000110000101001110

num = 12345678

#여기부터 작성

print("10진수 ===> ", num)
print("16진수 ===> ", hex(num))
print(" 8진수 ===> ", oct(num))
print(" 2진수 ===> ", bin(num))

a_2 = 100
b_2 = 200
print(a_2>b_2) #false

a_3 = "파이썬"
a_3 #'파이썬'
print(a_3) #파이썬
# print("오늘은"+27+"일 입니다") # concatenate error 발생, 문자에 정수를 붙일 수 없어 str화 시켜야함.
print("오늘은 "+str(27)+"일 입니다")

#이스케이프 시퀀스
a = '파이썬 \n만세'
print(a)

a = """파이썬
만세"""
a
print(a)

#실수 변환
# float() 사용