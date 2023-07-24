# Q3) 두수를 입력받아 첫번째 수가 두번째 수의 배수인지 출력하시요.
num1, num2 = int(input("Enter an Integer1: ")), int(input("Enter an Integer2: "))

if (num1 % num2) == 0:
    print("%d는 %d의 배수임" %(num1,num2))
else:
    print("%d는 %d의 배수아님" %(num1,num2))
    