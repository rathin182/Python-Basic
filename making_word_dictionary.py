d = {
    "villa" : "house",
    "chair":"kursi",
    "Tv":"durdarsan"

}

print("option are ", d.keys())

a = str(input("enter your Word: "))
a = a.lower()
print("Your Answer is", d.get(a))