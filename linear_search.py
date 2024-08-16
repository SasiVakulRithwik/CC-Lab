def linear_search(a, key):
    for i in range(len(a)):
        if key == a[i]:
            print(f"{key} found at the index {i}")
            return i
    print(f"{key} not found")
    return -1


a = [1,2,5,235,2,52,5,62,5,56,16,246,1,562,561,6,265,16,1]
linear_search(a, 33)