x = int(input('Enter number to check this number is prime or not : '))

for i in range(2,x):
    if x%i==0:
        print(f'{x} is not prime number...')
        break

else:
    print(f'{x} is prime number...')