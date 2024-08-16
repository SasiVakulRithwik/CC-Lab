def ibinary_search(a, key):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if key == a[mid]:
            print(f"{key} found the index {mid}")
            return mid
        elif key > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print(f"{key} not found")
    return -1


def rbinary_search(a, key, left, right):
    mid = left + (right - left) // 2
    if left <= right:
        if a[mid] == key:
            print(f"{key} found the index {mid}")
            return mid
        elif key > a[mid]:
            rbinary_search(a, key, mid+1, right)
        else:
            rbinary_search(a, key, left, mid-1)
    else:
        print(f"{key} not found")
        return -1


a = [1,2,5,235,2,52,5,62,5,56,16,246,1,562,561,6,265,16,1]
a.sort()
key = 52
print(f"Sorted list {a}")
ibinary_search(a, key)
rbinary_search(a, key, 0, len(a)-1)