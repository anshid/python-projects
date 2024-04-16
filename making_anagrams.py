def makeAnagram(a,b):
    a=list(a)
    b=list(b)
    
    #finding common characters in both string
    #and removing common characters from b
    common_char=[]
    for i in range(len(a)):
        if a[i] in b:
            common_char.append(a[i])
            b.remove(a[i])
    
    #Removing common characters from a
    c=common_char
    for i in range(len(c)):
        if c[i] in a:
            a.remove(c[i])
    
    #Extra characters remaining in both a and b
    extra_char=a+b
   
    return len(extra_char)
    

a = input("Enter first string: ")
b = input("Enter second string: ") 

print(makeAnagram(a,b))
