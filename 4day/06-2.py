# Q3) 두수를 입력받아 첫번째 수가 두번째 수의 배수인지 출력하시요.
num1 = int(input("Enter an Integer1: "))
num2 = int(input("Enter an Integer2: "))

if (num1 % num2) == 0:
    print("배수임")
else:
    print("배수 아님")
    