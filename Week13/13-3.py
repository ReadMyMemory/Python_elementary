contact = {}

while True:
    name = input("(입력모드)이름을 입력하시오: ")

    # 공백 입력. 검색 모드로 넘어감
    if not name:
        break

    # 입력모드 로직 실행
    else:
        # 정상) 딕셔너리에 존재하지 않는 이름이라면 새롭게 추가 가능. 이름과 전화번호 추가
        if name not in contact:
            phone = int(input("전화번호를 입력하시오: "))
            contact[name] = phone

        # 예외) 이미 존재하는 이름(key)라서 딕셔너리에 새로운 값을 추가할 수 없는 경우
        else:
            print("이미 존재하는 이름입니다. 전화번호를 추가할 수 없습니다.")

while True:
    name = input("(검색모드)이름을 입력하시오: ")

    # 공백 입력. 프로그램 종료
    if not name:
        break

    # 검색모드 로직 실행
    else:
        # 정상) 딕셔너리에 존재하는 이름이라면 전화번호 검색 가능.
        if name in contact:
            print("%s의 전화번호는 %d입니다." % (name, contact[name]))

        # 예외) 딕셔너리에 존재하지 않는 이름이라 전화번호 검색 불가능.
        else:
            print("저장되지 않은 이름입니다. 전화번호를 찾을 수 없습니다. ")


