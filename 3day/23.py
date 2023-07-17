#내장함수
dic = {"이름":"홍길동", "나이":"31", "주소":"부산", "이메일":"star@네이버"}
print(dic)
print(dic["이름"])
#key 이름표만 출력
print(dic.keys())
#value만 출력
print(dic.values())
print(dic.items())
#값으로서 그에 맞는 value출력
print(dic.get("이름"))
#존재 유무를 확인하는 방법
print("전화번호" not in dic)
print("이름" not in dic)
#print("전화번호", in dic)
print("이름" in dic)
dic.clear()
print(dic)
