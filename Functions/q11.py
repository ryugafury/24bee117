list1 =[]
list2=[]
list3=[]
def create_list(l1,l2,l3):
    l1=[]
    l2=[]
    
    n = int(input("Enter the range of the list"))
    for i in range(1,n+1):
        l1.append(int(input("Enter the values of list one")))
    for j in range(1,n+1):
        l2.append(int(input("Enter the values of list two")))
    s1=set(l1)
    s2=set(l2)
    l3=[s1.intersection(s2)]
    
    print(l3)
   
create_list(list1,list2,list3)