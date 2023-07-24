# Q1) 정수 하나를 입력받아 5의 배수인 경우 출력하시오.
number = int(input("Enter an Integer: "))
if (number % 5) == 0:
    print("%d는 5의 배수임." %number)
else:
    print("%d는 5의 배수아님." %number)
    
    