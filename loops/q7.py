print("Pulkit mantri\n24BEE117")

n = int(input("Enter the value of n"))
r =int(input("Enter the value of r"))
def nCr(a,b):
    fact =1
    ract=1
    tact=1
    for i in range (1,a+1):
        fact = fact*i
    for j in range (1,b+1):
        ract=ract*j
    for k in range(1,(a-b)+1):
        tact=tact*k
    l = ract *tact
    k=fact//l
    print(f"The nCr value is {k} ")
nCr(n,r)

def nPr (a,b):
    fact =1
    tact =1
    for i in range (1,a+1):
        fact = fact *i
    for j in range (1,(a-b)+1):
        tact=tact*j
    f = fact//tact
    print(f"The nPr value is {f}")
nPr(n,r)
