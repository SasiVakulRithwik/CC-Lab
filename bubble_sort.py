def bubble_sort(a):
    n = len(a)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                swapped = True
                a[j], a[j+1] = a[j+1], a[j]
        if not swapped:
            break
    print(a)

a = [1,2,5,235,2,52,5,62,5,56,16,246,1,562,561,6,265,16,1]
bubble_sort(a)