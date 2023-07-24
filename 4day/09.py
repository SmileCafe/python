#딕셔너리의 key만 입력하면 값이 출력된다.
#input 2개 입력: 단어 입력, 뜻 입력
#입력한 단어가 eng_dict에 없으면 에러 메세지
#있다면 그 뜻이 맞는가 비교하여 정답입니다. 아니면 틀렸습니다.

eng_dict = {
    "money":"돈",
    "variable":"변수",
    "function":"함수",
    "lucky":"행운",
    "star":"별"
}

input_str = input("Enter one or two values separated by a space: ")

if " " in input_str: 
    value1, value2 = input_str.split()
    if value2 == eng_dict[value1]:
        print("right!")
    else:
        print("wrong!")
    
else:
    value1 = input_str
    if value1 in eng_dict:
        print(eng_dict[value1])
    






 