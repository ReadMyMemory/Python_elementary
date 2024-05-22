std_list = {'이하나': 2024, '이두나': 2023}
print(std_list['이두나'])  # 해당 키값을 가지는 key-value 출력
print(std_list['이두나'] == 2019)  # 조건 판단 True or False
print(std_list)  # 딕셔너리 전체출력
print(std_list.keys())  # 키만 뽑기
print(std_list.values())  # 값만 뽑기

print("-----------------------")

item = {'커피': 10, '사무용품': 20, '종이컵': 25, '책': 40, '슬리퍼': 15}
ans = input("재고 물건의 이름을 입력하세요: ")
print("재고 물건 \'%s\'는 %d개 있습니다." % (ans, item[ans]))


