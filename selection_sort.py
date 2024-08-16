def pselection_sort(a):
    n = len(a)
    for i in range(n-1):
        sub=a[i:]
        min_i = i+sub.index(min(sub))
        a[i], a[min_i] = a[min_i], a[i]
    print(a)


def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        min_i = i
        for j in range(i,n):
            if a[min_i] > a[j]:
                min_i = j
        if min_i != i:
            a[i], a[min_i] = a[min_i], a[i]
    print(a)


a = [1,2,5,235,2,52,5,62,5,56,16,246,1,562,561,6,265,16,1]
selection_sort(a)
