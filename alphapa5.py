n = 6
for i in range(1,n):
    for j in range(n-i):
        print(end='  ')
    m = 65
    for k in range(1,2*i):
        print(end=chr(m)+' ')
        m+=1
    print()

print()