print("Pulkit mantri\n24BEE117")

for a in range (1,31):
    for b in range (a+1,31):
        for c in range (b+1,31):
            if((a*a)+(b*b)==(c*c)):
                print(f"The pythagorean triplet is {a},{b},{c}")
