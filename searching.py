def linsearch(a, target):
    count = 1
    for i in range(len(a)):
        print("Iteration:", count)
        count += 1
        if a [i] == target:
            return i
        
    return -1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
returned_value = linsearch(a, target)
if returned_value == -1:
    print("Element not found")
else:
    print(f"Element found at index {returned_value}")