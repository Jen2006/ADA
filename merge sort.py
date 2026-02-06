import random
import time
import matplotlib.pyplot as pit


# find mid 
# divide into two halves depended on mid
# recurse it
# call merge fuction
# display output

def merge_sort(arr):
    if len(arr)==1:
        return arr
    

    mid =len(arr)//2
    left = merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result=[]

    i=j=0

    while i< len(left) and j<len(right):
      if left[i]<right[j]:
          result.append(left[i])
          i+=1
      else:
          result.append(right[j])
          j+=1



    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr=[38,27,43,3,9,10]
sorted_arr=merge_sort(arr)
print(sorted_arr)

#time analysis

