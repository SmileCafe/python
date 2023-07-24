# 정수 하나를 입력받아 절대값을 구하시오.
number = int(input("Enter an Integer for absolute number: "))

if number < 0:
    print ("%d의 절대값은 %d입니다. %(number,-number)")
else:
    print (number)
