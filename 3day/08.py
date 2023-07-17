print("%s, %s, %s" %('하나', '둘', '셋')) #개수대로 순서에 맞게 입력해야 함.
print("%d, %d, %d" %(1, 2, 3))
print("작품번호:%5d, 작품선호도:%6.2f" %(365, 9.228))

#문제
print("체질량지수(BMI)를 계산해 봅시다.")
weight = int(input("체중을 정수로 입력하세요: "))
height = float(input("키를 입력하세요: "))
bmi = weight / (height*height)
comment = "당신의 BMI는 %d/(%.2f*%.2f)이므로 %6.2f이다."
print(comment %(weight, height, height, bmi))