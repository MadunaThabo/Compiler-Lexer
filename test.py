def elementInArray(arr, x):
    for i in range(0,10):
        for k in range(i,10):
            i+=k
            print(i)
            break
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 4
elementInArray(arr, x)