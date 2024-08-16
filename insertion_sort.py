def insertion_sort(a):
    n = len(a)
    for i in range(1,n-1):
        j = i
        while j >= 0 and a[j]<=a[j-1]:
            j -= 1
            a[j], a[j-1] == a[j-1], a[j]
        
        
