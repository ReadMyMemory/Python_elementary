# 2차시 학습 활동 첨부된 사진 파일 확인
# 사용자가 입력한 숫자를 더하는 프로그램, yes라고 답하는 동안에만 숫자를 입력받고, no라고 답하면 모든 숫자의 합을 출력.

hap = 0
hap += int(input("숫자를 입력하시오 : "))
while True:
    if input("계속?(yes/no) :  ") == "yes":
        hap += int(input("숫자를 입력하시오 : "))
    else: # yes 이외의 값이 입력 되었을 때, 정상적인 상황에서의 응답은 no 라고 생각하여 처리.
        print(hap)
        break
