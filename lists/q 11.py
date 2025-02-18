print("Pulkit mantri\n24BEE117")

'''def perfect():
    l=[]
  
    c=0
    d=0
    
    n = int(input("Enter the range"))
    for i in range (n):
        l.append((int(input("Enter the values of list"))))
       

    
    for a in l:
        j=a
        sum=0
       
        
        while a>0:
            sum+=a%10
            a//=10
        if j==sum:
            c+=1
        else:
            d+=1
    print(f"The number of perfect numbers is {c}")
    print(f"the number of non perfect numbers is {d}")
perfect()'''
def perfect():
    l = []  # Initialize the list to store numbers
    c = 0  # Count of "digit-sum-perfect" numbers
    d = 0  # Count of non-"digit-sum-perfect" numbers
    
    n = int(input("Enter the range: "))
    
    # Collect the numbers from the user
    for i in range(n):
        l.append(int(input(f"Enter the value of the list at index {i+1}: ")))
    
    # Loop through each number in the list to check the digit sum
    for a in l:
        original_a = a  # Save the original value of a
        sum_digits = 0  # Reset sum of digits for each number
        
        # Sum the digits of the number
        while a > 0:
            sum_digits += a % 10
            a //= 10  # Use integer division to remove the last digit
        
        # Check if the sum of digits is equal to the original number
        if original_a == sum_digits:
            c += 1
        else:
            d += 1
    
    # Output the results
    print(f"The number of digit-sum-perfect numbers is {c}")
    print(f"The number of non-digit-sum-perfect numbers is {d}")

# Call the function to test
perfect()
