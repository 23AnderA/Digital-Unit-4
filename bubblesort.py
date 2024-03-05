def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            n1 = arr[j]
            n2 = arr[j + 1]

            if n1 > n2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
input_list = [2, 8, 5, 3, 9, 4, 1]
bubble_sort(input_list)
print("Sorted list:", input_list)
