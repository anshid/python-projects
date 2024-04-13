def count(string,alph):
    c=0
    for b in string:
        if b==alph:
            c=c+1
    return c



string=input("Enter the string:")
alph=input("Enter the alphabet to count")

print(count(string,alph))
