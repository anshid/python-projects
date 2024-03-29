word=input("Enter the sentence:")

alphabets = []

for _ in word:
    alphabets.append(_)

dict={}

for a in alphabets:
    count = 0
    for b in word:
        if b==a:
            count = count + 1
    dict[a]=count


print(dict)
