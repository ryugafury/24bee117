print("Pulkit mantri\n24BEE117")

def fact():
    l=[]
    
    n = int(input("Enter the range"))
    for i in range(n):
        l.append((int(input("Enter the values of the list"))))
        
    for a in l:
        fact =1
        for j in range(1,a+1):
            fact=fact*j
        print(f"The factorial of numbers{a} are {fact}")
fact()
    
