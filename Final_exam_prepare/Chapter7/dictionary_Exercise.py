# 딕셔너리는 자바에서의 해시맵이라고 생각해도 좋다. key value 값을 가지는 그런 존재임.
# 딕셔너리는 순서가 없다. 그 점이 차이점이다.
# 딕셔너리는 키가 유일하다. 그래서 같은 키를 사용하면 나중에 추가한 것만 남는다
# 딕셔너리는 삭제할 때 키를 기준으로 삭제한다. del(dict['학과'])
# 딕셔너리 접근은 2가지 방법이 잇다. dict['학과']와 dict.get('학과')
# 모든 키를 보고 싶으면 dict.keys() 하면 됨.
import operator

dict = {'학과': 1, '학번': 3, '이름': 5}
print(dict.keys())  # dict_keys(['학과', '학번'])
# dict_keys가 보기 싫으면 리스트 형변환 시키면 된다.
print(list(dict.keys()))  # ['학과', '학번']
# dict.values() 하면 리스트로 반환, dict.items() 하면 튜플로 반환한다
print(dict.values())  # 리스트화 dict_values([1, 3])
# 역시나 보기 싫으면 list로 감싸서 형변환시키면 dic_values 사라짐
print(dict.items())  # 튜플화 dict_items([('학과', 1), ('학번', 3)])
# 딕셔너리 안에 키가 있는지 없는지는 in으로 판단
print('학과' in dict)  # True
print('학과' not in dict)  # False
# 아까 딕셔너리에 순서는 없다 했지만, 전체 출력할 때 정렬하고 싶으면 리스트화하면 된다.
print(sorted(dict.items(), key = operator.itemgetter(0)))  # [('이름', 5), ('학과', 1), ('학번', 3)]
# 핵심은 리스트로 출력되고, key-value는 튜플화가 된다.
# sorted(key-value를 items()로 튜플화, key = 뭐로 정렬? itemgetter(0)은 튜플의 맨 앞인 key고 itemgetter(1)은 그 뒤엔 value가 되겠다.


# 딕셔너리의 특징을 이용한 세트라는 게 있다. 딕셔너리의 키만 모였다고 생각하면 된다.
# 리스트의 중복을 없애기 위해 set(list)를 출력하면 중복이 제거된다.


