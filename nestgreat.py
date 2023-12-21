num1 =int(input('enter num1 value:-'))
num2 =int(input('enter num2 value:-'))
num3 =int(input('enter num3 value:-'))
if num1>num2 and num1>num3:
    if num2>num3:
        print('num2 is second greater')
    else:
        print('num3 is  second greater')
elif num2>num3:
    if num1>num3:
        print('num1 is secontd greater')
    else:
        print('num3 is secound greater')
else:
    if num1>num2:
        print('num1 is second greater')
    else:
        print('num2 is second greater')
    

  