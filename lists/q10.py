print("Pulkit mantri\n24BEE117")

list =[]
def prime(l):
    l=[]
    n=int(input("Enter the range"))
    c=0
    d=0
    e=0
    for i in range(n):
        l.append((int(input("Enter the elements of the list"))))
        a=l[i]
    for a in l:
        for j in range (1,a+1):
            if(a%j==0):
                c+=1
             
        if(c==2):
            d+=1
        
        else:
           e+=1
        
    print(f"The number of prime numbers is {d}")
    print(f"The number of co2mposite number is {e}")
prime(list)
