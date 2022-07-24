for r in range(5):
    for c in range(r+1):
        if (r+c)%2 != 0:
            print(end='0 ')
        else:
            print(end='1 ')
    print()