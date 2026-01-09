# Algorithm:
# 1. Input element into list/array
# 2. Enter the element you want to find 
# 3. Start with a for loop 
#    if the arr[i]== key 
#    return true and position
#    else return False
# 4. print the output

arr = []
n = int(input("Enter number of elements in the array: "))

for i in range(n):
    arr.append(int(input("Enter the array elements: ")))
    
key = int(input("Enter the element to be searched: "))

found = False

for i in range(n):
    if arr[i] == key:
        print(f"Element found at the position {i + 1}")
        found = True
        break
    
if not found:
    print("Element not found in the array")   
      