

#동전교환기 예제, 내가 작성

amount = int(input("교환할 돈은 얼마? "))

print("500원짜리 ==> "+str(int(amount / 500))+"개")
amount %= 500
print("100원짜리 ==> "+str(int(amount / 100))+"개")
amount %= 100
print("50원짜리 ==> "+str(int(amount / 50))+"개")
amount %= 50
print("10원짜리 ==> "+str(int(amount / 10))+"개")
amount %= 10
print("바꾸지 못한 잔돈 ==> "+str(amount)+"개")


#정석 코드

won, c500, c100, c50, c10 = 0,0,0,0,0
won = int(input("교환할 돈을 입력하세요 : "))

c500 = won//500
won = won%500
c100 = won//100
won = won%100
c50 = won//50
won = won%50
c10 = won//10
won = won%10

print("500원 동전은 ==> %d개" % c500)
print("100원 동전은 ==> %d개" % c100)
print("50원 동전은 ==> %d개" % c50)
print("10원 동전은 ==> %d개" % c10)
print("바꾸지 못한 동전은 ==> %d개" % won)
