# 1st method
n = 5
for i in range(1,6):
    print('  '*(n-i)+'* '*i)
    
for i in range(4,0,-1):
    print('  '*(n-i)+'* '*i)

print()

# 2nd method
# n = 6
# for i in range(1,n):
#     for j in range(i,n-1):
#         print(end='  ')
#     for j in range(i):
#         print(end='* ')
#     print()

# for i in range(2,n):
#     for j in range(i-1):
#         print(end='  ')
#     for j in range(n-i):
#         print(end='* ')
#     print()

