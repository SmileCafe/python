num = 0
while True:
    print("""
          ====== 메뉴 ======
          1. 정수 입력
          2. 입력된 정수 출력
          3. 종료
          """)
    select = int(input("메뉴 선택: "))
    if select == 1:
        num = int(input("정수 입력: "))
    elif select == 2:
        print("입력된 정수는 {}입니다." .format(num))
    else:
        break