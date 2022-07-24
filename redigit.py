try:
    x = int(input('Enter number : '))
    x = str(x)
    y = x[::-1]
    x = int(y)
    print(x)
except:
    print('invalid input!')