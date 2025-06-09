def quicksort (a):
    if len(a) <= 1:
        return a
    else:
        left = []
        right = []
        pivot = a[-1]
        for i in a [:-1] :
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quicksort(left) + [pivot] + quicksort(right)
    
a = [78, 34, 56, 12, 22, 11]
print("Unsorted array:", a)
print("Sorted array:", quicksort(a))