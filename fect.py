x = int(input('Enter number to get fectorial : '))+1
fect = True

for i in range(2,x):
    fect*=i

print(f'{x-1}! : {fect}')
