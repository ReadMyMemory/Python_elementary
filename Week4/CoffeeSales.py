#교재 문제,커피 전문점에서 판매 개수 입력받아 총매출 출력하기

#가격 선입력
americano_price = 2000
caffelatte_price = 3000
capuchino_price = 3500

americano_sales, caffelatte_sales, capuchino_sales, amount = 0,0,0,0

americano_sales = int(input("아메리카노 판매 개수 : "))
caffelatte_sales = int(input("카페라떼  판매 개수 : "))
capuchino_sales = int(input("카푸치노 판매 개수 : "))

amount += americano_price * americano_sales
amount += caffelatte_price * caffelatte_sales
amount += capuchino_price * capuchino_sales

print("총 매출액은 %d원 입니다." % amount)



