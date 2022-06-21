exam = int(input("Enter Exam consume number:\n"))

sub1 = int(input("Enter Your first number: "))
sub2 = int(input("Enter Your Second number: "))
sub3 = int(input("Enter Your Third number: "))
b = 30/100
d = 40/100
e = exam*d
c = exam*b
z = sub1 + sub2 + sub3
# print(c)
if (sub1<c or sub2<c or sub3<c):
    print("you are fail less sorry")
elif (z<d):
    print("fail your combined number is less the 40%")
else:
    print("you are pass")