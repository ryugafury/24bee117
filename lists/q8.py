print("Pulkit mantri\n24BEE117")

list=[]
def num (l):
    n = int(input("Enter the range"))
    l= []
    c=0
    d=0
    for i in range (n):
        l.append(int(input("Enter the values of the list")))
        if(l[i]%2==0):
            c+=1
        else:
            d+=1
    print(f"The number of odd numbers is {d}")
    print(f"The number of even numbers is{c}")

num(list)
