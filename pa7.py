x = 7
for i in range(1,x+1):
    if i%2!=0:
        print(' '*(x-i)+'* '*i)

x = 5
for i in range(x,0,-1):
    if i%2!=0:
        print(' '*(x-i)+'  '+'* '*i)
