print("Pulkit mantri\n24BEE117")

a = input("Enter a string")
b = len(a)
a.lower()
c=0
d=0
for i in a:
    if('a'<= i <= 'z'):
        c+=1
    else:
        d+=1
print(f"The number of alphabets is {c}")
print(f"The number of digits is {d}")
