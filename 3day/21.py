people = {"박세웅":"야구", "손흥민":"축구", "김연아":"스케이트"}
print(people)
print(type(people))
people2 = {"name":"홍길동", "age":20}
print(people2["name"])
print(people2["age"])
people2["name"] = "아이유"
people2["age"] = 27
print(people2)
people2["job"] = ["가수", "배우", "모델"]
#아이유의 직업은 가수,배우,모델입니다를 고급포매팅으로 print하세요.
#print("{0}의 직업은 {1}입니다." .format())
people3 = people2["job"]
print("아이유의 직업은 {},{},{} 입니다." .format(people3[0], people3[1], people3[2]))
print(type(people3))