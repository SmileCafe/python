# 현재 건물에는 엘리베이터 2대가 있고,
# A 엘리베이터는 5층에 B 엘리베이터는 7층에 있다.
# 현재 내가 있는 층수를 눌러 가장 가까운 엘리베이터를 움직이시오.
# (층 수의 개수가 차이가 같은 경우 B 엘리베이터가 움직인다.)
# (절대값을 사용해서 A와 B 엘리베이터의 차이를 구하여 움직인다.)

myStory = int(input("Enter your story: "))
aStory = 5
bStory = 7

A = aStory - myStory
B = bStory - myStory

if aStory != 5 and bStory != 7:
    if abs(A) < abs(B):
        print("A elevator is coming for ya")
    else:
        print("B elevator is coming for ya")
else:
    if myStory == 5:
        print("A Elevator is in front of ya")
    else:
        print("B Elevator is in front of ya")
    