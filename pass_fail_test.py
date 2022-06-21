m = int(input("Enter Your Exam Consume Number: "))

stu = int(input("Enter your 1st Number: "))
stu2 = int(input("Enter your 2st Number: "))
stu3 = int(input("Enter your 3st Number: "))

f = 30/100
h = 40/100
k = h*m
g = f*m
u = stu+stu3+stu2
# print(g)
if (stu<g or stu2<g or stu3<g):
     print("you are fail")
elif(u<k):
    print("you are fail")
else:
    print("you are pass")