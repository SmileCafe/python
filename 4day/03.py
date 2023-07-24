print("오늘도 지각이다. 대중교통을 탈까? 택시를 탈까?")
money = input("택시 탈 돈을 가지고 있는가?[y / n]:")
if money == 'n':
    print("어쩔 수 없지... 대중교통이다 \n지하철, 버스 중 뭘 타지?")
    time = input("출근 시간인가? [y / n]:")
    if time == "y":
        print("지하철을 타고 가야겠다!")
    else:
        print("버스 타고 가야지!")
else:
    print("남는 게 돈이야 택시타고 얼란 가야셌다")