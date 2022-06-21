t = input("enter commnat:-\n")
t = t.lower()
if("make a lot of money" in t):
    print("this is a spam")
elif("buy now" in t):
    print("this is a spam")
elif("subscribe this" in t):
    print("this is a spam")
elif("click this" in t):
    print("this is also a spam")
else:
    print("thanx for comment")