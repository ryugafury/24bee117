print("Pulkit mantri\n24BEE117")

a=[]
b=[]
c=[]
for i in range (5):
    a.append((int(input("Enter 5 numbers "))))
    d = a[i]
for j in range (5):
    b.append((int(input("Enter 5 numbers for second list "))))
    e =b[j]
for i in a :
    if i not in b:
        c.append(i)
print(c)
