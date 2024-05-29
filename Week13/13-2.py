storage = { '우유': 0, '종이컵': 0, '책': 0, '커피음료': 0, '콜라': 0, '펜': 0}

while True:
    print("***********************")
    print("0: 종료")
    print("1: 재고 추가")
    print("2: 삭제")
    print("3: 재고 목록 보기")
    print("***********************")
    print("")
    choice = int(input("무엇을 하시겠습니까?"))

    if choice == 0:
        break
    elif choice == 1:
        item = input("물건의 이름을 입력하세요: ")
        quantity = int(input("몇 개를 추가하시겠습니까? "))

        if item in storage:
            storage[item] += quantity
        else:
            storage[item] = quantity
        print("")
        print("# 재고 목록 #")
        for key, value in storage.items():
            print(f"{key} {value}")
        print("")
    elif choice == 2:
        item = input("물건의 이름을 입력하세요: ")
        if item in storage:
            quantity = int(input("몇 개를 삭제하시겠습니까? "))
            if quantity > storage[item]:
                print(f"{item}의 재고가 부족합니다. 현재 재고: {storage[item]}")
            else:
                storage[item] -= quantity
                if storage[item] == 0:
                    del storage[item]
                print(f"{item}이(가) {quantity}개 삭제되었습니다.")
        else:
            print(f"{item}이(가) 목록에 없습니다.")
        print("")
        print("# 재고 목록 #")
        for key, value in storage.items():
            print(f"{key} {value}")
        print("")
    elif choice == 3:
        print("")
        print("# 재고 목록 #")
        for key, value in storage.items():
            print(f"{key} {value}")
        print("")
    else:
        print("잘못된 번호입니다. 올바른 번호를 입력하세요.")
