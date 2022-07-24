# 1st method
for i in range(65,70):
    print(end=(chr(i)+' ')*(i-64))
    print()

print()
# 2nd method
for i in range(65,70):
    for j in range(65,i+1):
        print(end=chr(i)+' ')
    print()