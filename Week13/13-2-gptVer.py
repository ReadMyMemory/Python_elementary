inventory = {
    "우유": 0,
    "종이컵": 0,
    "책": 0,
    "커피음료": 0,
    "콜라": 0,
    "펜": 0
}

print("# 재고 목록 #")
for key, value in inventory.items():
    print(f"{key} {value}")
print("")

while True:
    print("***********************")
    print("0: 종료")
    print("1: 재고추가")
    print("2: 삭제")
    print("***********************")
    print("")
    choice = int(input("무엇을 하시겠습니까?"))

    if choice == 0:
        break
    elif choice == 1:
        item = input("물건의 이름을 입력하세요: ")
        quantity = int(input("몇 개를 추가하시겠습니까? "))

        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity

        print("# 재고 목록 #")
        for key, value in inventory.items():
            print(f"{key} {value}")
        print("")
    elif choice == 2:
        item = input("물건의 이름을 입력하세요: ")
        if item in inventory:
            quantity = int(input("몇 개를 삭제하시겠습니까? "))
            if quantity > inventory[item]:
                print(f"{item}의 재고가 부족합니다. 현재 재고: {inventory[item]}")
            else:
                inventory[item] -= quantity
                if inventory[item] == 0:
                    del inventory[item]
                print(f"{item}이(가) {quantity}개 삭제되었습니다.")
        else:
            print(f"{item}이(가) 목록에 없습니다.")

        print("# 재고 목록 #")
        for key, value in inventory.items():
            print(f"{key} {value}")
        print("")
    else:
        print("올바른 번호를 입력하세요.")
