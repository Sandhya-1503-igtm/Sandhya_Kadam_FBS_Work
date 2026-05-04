n = 5



for i in range(1, n+1):
    # spaces
    for s in range(n - i):
        print(" ", end=" ")
    
    # increasing (1 to i)
    for j in range(1, i+1):
        print(j, end=" ")
    
    # decreasing (i-1 to 1)
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    
    print()