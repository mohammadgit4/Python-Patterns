try:
    x = int(input('Enter number to check palindrome or not : '))
    y = str(x)
    if str(x) == y[::-1]:
        print(f'{x} is palindrome Number')
    else:
        print(f'{x} is not palindrome Number')

except:
    print('invalid input!')