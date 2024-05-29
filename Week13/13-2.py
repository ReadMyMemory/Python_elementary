storage = {'우유': 0, '종이컵': 0, '책': 0, '커피음료': 0, '콜라': 0, '펜': 0}

while True:
    print("***********************")
    print("0: 종료")
    print("1: 재고 추가")
    print("2: 삭제")
    print("3: 재고 목록 보기")
    print("***********************")
    print("")
    choice = int(input("무엇을 하시겠습니까?"))

    # 0. 종료 로직
    if choice == 0:
        break

    # 1. 재고 추가 로직
    elif choice == 1:
        item = input("물건의 이름을 입력하세요: ")

        # 정상) 존재하는 재고 품목이라면, 정상적인 로직 진행
        if item in storage:
            quantity = int(input("몇 개를 추가하시겠습니까? "))
            storage[item] += quantity
            print("%s이(가) %d개 추가되었습니다." % (item, quantity))

        # 예외) 새로운 재고 품목 추가가 아니라고 문제에 주어졌으므로 존재하지 않는 품목이라면
        else:
            print("%s은(는) 존재하지 않는 항목입니다. 새로운 항목을 추가할 수 없습니다." % item)

        # 재고 목록을 출력
        print("")
        print("# 재고 목록 #")
        for key, value in storage.items():
            print("%s %s" % (key, value))
        print("")

    # 2. 재고 삭제 로직
    elif choice == 2:
        item = input("물건의 이름을 입력하세요: ")

        # 정상) 존재하는 재고 품목이라면, 정상적인 로직 진행
        if item in storage:
            quantity = int(input("몇 개를 삭제하시겠습니까? "))

            # 예외) 삭제할 재고가 현재 재고보다 많은 경우
            if quantity > storage[item]:
                print("%s의 재고가 부족합니다. 현재 남아있는 재고는 %d 입니다." % (item, storage[item]))
            else:
                storage[item] -= quantity
                print("%s이(가) %d개 삭제되었습니다." % (item, quantity))

        # 예외) 삭제를 시도하는 재고 품목이 존재하지 않는 경우
        else:
            print("%s은(는) 존재하지 않는 항목입니다. 없는 항목의 재고를 삭제할 수 없습니다." % item)

        # 재고 목록을 출력
        print("")
        print("# 재고 목록 #")
        for key, value in storage.items():
            print("%s %s" % (key, value))
        print("")

    # 3. 재고 목록 조회 로직
    elif choice == 3:

        # 재고 목록을 출력
        print("")
        print("# 재고 목록 #")
        for key, value in storage.items():
            print("%s %s" % (key, value))
        print("")

    # 예외) 0, 1, 2, 3이 아닌 다른 값을 입력한 경우
    else:
        print("잘못된 번호입니다. 올바른 번호를 입력하세요.")
