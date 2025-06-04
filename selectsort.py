# Selection Sort Algorithm Implementation
def selectionsort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
                
        a [i], a[min_index] = a[min_index], a[i]
    
    return a
       
a = [64, 25, 12, 22, 11]
print("Unsorted array:", a)
print("Sorted array:", selectionsort(a))


# Bubble Sort Algorithm Implementation

def bubblesort(a):
    n = len(a)
    for i in range (n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                
    return a

a = [67, 34, 25, 12, 22, 11]
print("Unsorted array:", a)
print("Sorted array:", bubblesort(a))

# Insertion Sort Algorithm Implementation

def insertionsort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            
        a[j + 1] = key
        
    return a

a = [78, 34, 56, 12, 22, 11]
print("Unsorted array:", a)
print("Sorted array:", insertionsort(a))