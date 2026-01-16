# Algorithm:
# 1. Enter elements into array
# 2. Select a key element
# 3. compare it the elements present to the left side of the key using inner for loop, swap if needed
# 4. use outer for loop to move the key to the next position
# 5 sort the elements
# 6. display        


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
       
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
       
        arr[j + 1] = key
        
    return arr


data = [45, 78, 32, 3, 2, 11, 45]
print("The sorted elements are:", insertion_sort(data))