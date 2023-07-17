kg = "BUSANIT"
address ="부산광역시 수영구 민락동"
start = 19
name = "송진우"
end = 22
height = 192.123456
age = 29
Phone = "010-5567-1430"

phone = Phone.split("-")
ph0 = phone[0]
ph1 = phone[1]
ph2 = phone[2]

print(kg.center(30, "☆"))
print("파이썬 강의: {}시 ~ {}시" .format(start-3, end-3))
print("본인 이름: %s" %name)
print("본인 나이: %d" %age)
print("핸드폰: {} - {} - {}" .format(ph0, ph1, ph2))
print("주소: %s" %address)
print("키: %5.2f" %height)
print(kg.center(30, "☆"))

