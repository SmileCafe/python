# 주민등록번호는
# 
# 성별정보는 1이면 1900년대 출생

# 출력)
# 생년월일 6자리: 901129
# 주민번호 뒷자리의 첫글자: 1
# 성별정보가 1이므로, 1990년생, 29살 입니다.

# 출력)
# 생년월일 6자리: 030517
# 주민번호 뒷자리의 첫글자: 3
# 성별정보가 3이므로, 2003년생, 16살 입니다.

str = input("Enter your Registeration Number: ")
value1, value2 = str.split("-")

if value2[0] == "1":
    age = 2023 - (1900 + int(value1[:2]))
    birthYear = 1900 + int(value1[:2])
    
    print(age)
    print("생년월일 6자리: %s" %value1[:6])
    print("주민번호 뒷자리의 첫글자: %c" %value2[0])
    print("성별정보가 %c 이므로, %d년생, %d살입니다." %(value2[0], birthYear, age))

elif value2[0] == "3":
    age = 2023 - (2000 + int(value1[:2]))
    birthYear = 2000 + int(value1[:2])
    
    print(age)
    print("생년월일 6자리: %s" %value1[:6])
    print("주민번호 뒷자리의 첫글자: %c" %value2[0])
    print("성별정보가 %c 이므로, %d년생, %d살입니다." %(value2[0], birthYear, age))
