# Q1) 국어, 영어, 수학 세과목의 성적을 입력받고 평균에 따른 등급을 출력하시오.

kor = int(input("국어"))
eng = int(input("영어"))
math = int(input("수학"))
avg = (kor + eng + math)/3

if 0 <= avg and avg <=100:
    if avg >= 90
        print("A")
    elif avg >= 80:
        print("B")
    elif avg >= 70:
        print("C")
    elif avg >= 60:
        print("D")
    else:
        print("F")
else:
    Print("Your iput is wrong")