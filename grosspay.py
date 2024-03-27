#Calculate gross pay
hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")

try:
  hrs=float(hrs)
  rate=float(rate)
  pay= hrs*rate
  print('Pay:',pay)
except:
  print('Error, please enter numeric input')


