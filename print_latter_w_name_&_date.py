a = ''' Dear <Name>,
you are selected <Date>'''
b = input("enter your name\n")
c = input("enter Date\n")
a = a.replace("<Name>", b )
a = a.replace("<Date>", c )
print(a)
