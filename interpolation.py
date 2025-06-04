def interpol (a,target):
    left = 0
    right = len(a) - 1
    count = 1
    while left <= right and a[left] <= target <= a[right]:
        print("Iteration:", count)
        count += 1
        pos = left + (right-left) * (target - a[left]) // (a[right] - a[left])
        if a[pos] == target:
            return pos
        elif a[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
            
    return -1

a = [2, 4, 5, 6, 7, 8, 9, 11, 13, 14,
15, 17, 18, 19, 21, 23, 24, 25, 27, 28,
29, 30, 31, 32, 33, 35, 37, 39, 40, 42,
44, 45, 47, 49, 51, 52, 54, 59, 61, 64,
66, 68, 70, 73, 75, 78, 80, 83, 87, 91]

target = 83
returned_value = interpol(a, target)
if returned_value == -1:
    print("Element not found")
else:
    print(f"Element found at index {returned_value}")
    