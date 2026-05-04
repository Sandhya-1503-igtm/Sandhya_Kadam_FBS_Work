n = 5

# upper part
for i in range(n):
    for j in range(n*2):
        if j == n-i-1 or j == n+i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# lower part
for i in range(n-2, -1, -1):
    for j in range(n*2):
        if j == n-i-1 or j == n+i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()