money = "부산 112 2014 9018 01입금 = 10억원"
Bank = money[:2]
Gejoua = money[3:-9]
Won = money[-4:]
print("은행:", Bank, ", 계좌번호:", Gejoua, ", 금액:", Won)