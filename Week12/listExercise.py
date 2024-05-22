#삭제, 재설정
aa = [10, 20, 30]
aa[1:2] = [200, 201] # 뒷 값을 []로 하면 del과 같은 효과를 낸다. 여러 인덱스를 동시에 삭제할 때 유용
print(aa)

del(aa[1])
print(aa)

print("-----------------")

bb = ['가', '나', '다']
print('가' in bb) # True
print('바' in bb) # False

print("-----------------")
# 그 외 메서드

#sort, 정렬한다. 기본은 오름차순
cc = [3, 71, 2, 15, 27, 44, 53, 62, 19]
print(cc)
cc.sort()
print(cc)

#pop, 리스트 맨 뒤 값을 뺀다.
cc.pop()
print(cc)

#remove, 일치하는 값을 삭제
cc.remove(3)
print(cc)

#len, 길이 출력
print(len(cc))

