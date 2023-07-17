#문자열 내장함수
str = "hello world"
print(str.count('o'))
print(str.count('l')) #문자 개수 세기
print(str.index('l'))
print(str.upper()) #대문자, lower()
a = ','
print(a.join(str))
str2 = "      ABC    "
print(str2.lstrip()) #공백 제거
print(str2.rstrip())

str3 = "Life is very easy"
print(str3.split(" "))
str4 = "Life:is:very:easy"
print(str4.split(":")) #리스트 자료형으로 변환

print(str3.replace("Life", "My Life"))
print(str3.center(30, '#')) # Center Alignment
print(str3.ljust(30, '#')) # Left Alignment
print(str3.rjust(30, '#')) # Right Alignment






