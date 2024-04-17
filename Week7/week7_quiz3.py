import random

computer = random.choice(['가위', '바위', '보'])
user = input("가위, 바위, 보를 입력하시오: ")
print("컴퓨터:", computer)

if user == '가위':
    if computer == '가위':
        print("비겼습니다.")
    elif computer == '바위':
        print("컴퓨터가 이겼습니다.")
    elif computer == '보':
        print("컴퓨터가 졌습니다.")
elif user == '바위':
    if computer == '가위':
        print("컴퓨터가 졌습니다.")
    elif computer == '바위':
        print("비겼습니다.")
    elif computer == '보':
        print("컴퓨터가 이겼습니다.")
elif user == '보':
    if computer == '가위':
        print("컴퓨터가 이겼습니다.")
    elif computer == '바위':
        print("컴퓨터가 졌습니다.")
    elif computer == '보':
        print("비겼습니다.")


