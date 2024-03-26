def check(number: int):
    if number % 7 == 0 or number % 5 == 0:
        return True
    elif number < 10:
        return False

    return check(number - 7) or check(number - 5)


for num in range(1, 1000):
    if check(num) == False:
        print(num)