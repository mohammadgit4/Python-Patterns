# 1st method
n = 6
m = 65
for i in range(1,n):
    for j in range(n-i):
        print(end='  ')
    for k in range(1,2*i):
        print(end=chr(m)+' ')
        m+=1
    print()


# 2nd method
# b = 65
# for i in range(0, 9, 2):
#     for j in range(8, -1, -1):
#         if j>i:
#             print(end=" ")
#         else:
#             print(end=chr(b)+" ")
#             b += 1
#     print()