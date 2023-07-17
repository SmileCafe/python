print("이번 달 저축액: {}만원" .format(30))
print("이번 달 저축액: {}만원" .format(50))
print("관리비 {}만원, 학원비 {}만원, 교재비 {}만원" .format(15, 30, 10))
print("관리비 {0}만원, 학원비 {1}만원, 교재비 {2}만원" .format(15, 30, 10))
print("관리비 {2}만원, 학원비 {0}만원, 교재비 {1}만원" .format(15, 30, 10))
print("{} {} {}" .format(3, "ABC", True)) #모든 자료형이 들어올 수 있음.
print("{:d}" .format(53))
print("{:15d}" .format(53))
print("{:20d}" .format(53))
print("{:05d}" .format(53))
print("{:05d}" .format(-53))
print("이름:{:<10}, 나이:{:<5}" .format("홍길동", 27)) #왼쪽 정렬
print("이름:{:>10}, 나이:{:>5}" .format("홍길동", 27)) #오른쪽 정렬
print("이름:{:^10}, 나이:{:^5}" .format("홍길동", 27)) #가운데 정렬
print("{:20.3f}" .format(53.45871213)) #실수 출력
print("{:20.2f}" .format(53.45871213))
print("{:20.1f}" .format(53.45871213))
