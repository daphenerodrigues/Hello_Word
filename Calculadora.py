Lista = [6, 2, 8, 4, 3, 10, 5, 19, 25, 31, 30, 45, 12, 75, 100, 92]

def bubble_sort(arr):
    n = len (arr)

        for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort(Lista))


inserindo código Python "Commit new file".
