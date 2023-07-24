# 주차장에 주차를 하려고 한다. 30분까지의 기본요금은 1000원이고
# 10분당 500원씩의 추가요금을 받는다.
# 주차한 시간을 입력받아 총 주차요금을 출력하시요.
# (% 나머지기호를 적절하게 사용)

# 출력)
# 주차한 시간을 입력하세요: 20
# 주차요금은 1000원입니다.

# 출력)
# 주차한 시간을 입력하세요: 50
# 주차요금은 2000원입니다.

# 출력)
# 주차한 시간을 입력하세요: 35
# 주차요금은 1500원입니다. 

uPrice = 1000
ePrice = 500
time = int(input("Enter how long you have parked in minutes: "))

if time <= 30:
    print("주차요금은 %d 입니다." %uPrice)
else:
    if (time % 10) != 0:
        price = uPrice + (ePrice * int((time-30)//10)) + ePrice
        print("주차요금은 %d 입니다." %price)
    else:
        price = uPrice + (ePrice * int((time-30)//10))
        print("주차요금은 %d 입니다." %price)


