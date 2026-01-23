from itertools import combinations

weights=[8,3,9,2]
values=[42,12,40,25]
capacity=10
n=len(weights)

best_value=0
best_subset=None

print("Subset\tTotal Weight\tTotal Value")
print("-"*52)


for r in range (n+1):
    for subset in combinations(range(n),r):
       total_w=sum(weights[i] for i in subset)
       total_v=sum(values[i] for i in subset)

       subset_display="{"+",".join(str(i+1) for i in subset)+"}"

       if total_w <= capacity:
           print(f"{subset_display:<15}{total_w:<15}${total_v}")
           if total_v > best_value:
               best_value=total_v
               best_subset=subset
           else:
               print(f"{subset_display:<15}{total_w:< 15} Not feasible")

print("\nOptimal solution")
print("Items selected:",{i+1 for i in best_subset})
print("Maximum value:$",best_value)