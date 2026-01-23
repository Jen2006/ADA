items = []
n = int(input("Enter number of items: "))

for i in range(n):
    v = int(input("Enter value: "))
    w = int(input("Enter weight: "))
    items.append((v, w))

capacity = int(input("Enter knapsack capacity: "))

# Sort by value/weight ratio (descending)
items.sort(key=lambda x: x[0] / x[1], reverse=True)

total_value = 0

for v, w in items:
    if capacity >= w:
        capacity -= w
        total_value += v
    else:
        total_value += v * (capacity / w)
        break

print("Maximum value:", total_value)

