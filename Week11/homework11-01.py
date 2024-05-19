# 1차시 학습 활동 SELF STUDY 6-7
# Code06-13.py를 while문으로 변경하기

hap, i = 0, 0

while i < 101: # 이건 True로 해도 상관 없을 듯
    hap += i
    if hap >= 1000:
        break
    i += 1  # while문으로 변경하며 i가 순차적으로 증가하도록 하는 코드 추가
print("1~100의 합계를 최초로 1000이 넘게 하는 숫자 : %d" % i)
