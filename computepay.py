def computepay(h, r):
    if h<=40:
        pay = h*r
    else:
        pay = 40*r+(h-40)*r*1.5
    return pay
        

hrs = input("Enter Hours:")
rate= input("Enter Rate:")

try:
    hrs = float(hrs)
    rate= float(rate)
except:
    print("Enter a valid Number")
    hrs=0
    rate=0

p = computepay(hrs, rate)
print("Pay", p)
