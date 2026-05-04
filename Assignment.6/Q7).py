n = 5

for i in range(1, n+1):
    ch = 'A'
    print("  " *(n-i), end=" ")
    for j in range(1, 2*i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    print()