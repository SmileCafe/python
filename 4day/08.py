# 버스는 10 정거장 미만일 경우에는 각 역의 평균 이동 시간이 2분 소요되며,
# 10 정거장이 넘으면 4분의 소요시간이 걸린다.
# 버스 정거장 수를 입력하면 소요시간을 계산하여 출력하시오.

station = int(input("Enter how many stations you should go through: "))
uTime = 0

if (station < 10):
    uTime = 2
else:
    uTime = 4

wTime = uTime * station

if (wTime < 60):
    print("It takes %d minutes" %wTime)
else:
    HH = wTime // 60
    MM = wTime % 60
    print("It takes %d hours and %d minutes." %(HH, MM))