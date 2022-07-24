from datetime import datetime
x = datetime.now()
for i in range(1,5001):
    print(i)

print()
print(datetime.now()-x)