import re
fname=input("Enter file name:")

try:
    fhand=open(fname)
except:
    print(f"File {fname} doesnt exist")

numbers=[]
for line in fhand:
    number_as_text_list = re.findall('[0-9]+', line)
    for n in number_as_text_list:
        numbers.append(int(n))
print(numbers)
total_sum=sum(numbers)
total_numbers=len(numbers)
print(f"Total number is {total_numbers}")
print(f"Total sum is {total_sum}")
