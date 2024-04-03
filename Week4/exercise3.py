inputMoney = int(input("투입한 돈: "))
goodsValue = int(input("물건값: "))

extraChange = inputMoney - goodsValue
c500 = extraChange // 500
extraChangeTemp = extraChange % 500
c100 = extraChangeTemp // 100

print("==============")
print("거스름돈: %d" % extraChange)
print("500원 동전의 개수: %d" % c500)
print("100원 동전의 개수: %d" % c100)
print("==============")