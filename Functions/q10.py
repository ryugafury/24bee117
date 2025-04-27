def frequency(str1):
    str1 = str1.upper() 
    char_dict = {}  

    c, d = 0, 0  

    for char in str1:
        if 'A' <= char <= 'Z':  
            c += 1
        else:
            d += 1
        
     
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

  
    sorted_dict = dict(sorted(char_dict.items()))

    print("Character Frequencies:", sorted_dict)
    print("Letter Count:", c)
    print("Non-Letter Count:", d)


str = input("Enter a string: ")
frequency(str)

    