print("Pulkit mantri\n24BEE117")

a = input("Enter a string")
def lower(b):
    result = ""
    for i in b:
        if('A'<=i<='Z'):
            result+= chr(ord(i)+32)
        else:
            result+=i
    print(f"Lowercase ={result}")
lower(a)
def upper(b):
    result = ""
    for i in b:
        if('a'<=i<='z'):
            result+= chr(ord(i)-32)
        else:
            result+=i
    print(f"Uppercase ={result}")
upper(a)
def toggle(b):
    result = ""
    for i in b:
        if('a'<=i<='z'):
            result+= chr(ord(i)-32)
        elif('A'<=i<='Z'):
            result+=chr(ord(i)+32)
        else:
            result+=i
    print(f"Toggle case ={result}")
toggle(a)
