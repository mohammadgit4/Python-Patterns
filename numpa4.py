m = 1
for i in range(1,4):
    for j in range(i,4):
        print(end='  ')
    for j in range(i):
        print(m, end=' ')
        m+=1
    for j in range(i-1):
        print(m, end=' ')
        m+=1
    print()
