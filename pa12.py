n = 6
m = 12
for i in range(n):
    for j in range(m):
        if i==0 or i==n-1 or j==0 or j==m-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()