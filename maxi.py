# Algorithm:
# 1. Start
# 2. Input numbers into a list  num[]
# 3. Assign first element to max element
#    num[0] -> max
# 4. Start with a for loop
#    If num[i] > max then   max=num[i]
# 5. End for loop
# 6. Print max


def maximun(num,n):
    max=num[0]

    for i  in range(1,len(num)):
        if num[i]>max:
            max=num[i]

    return max

num=[]
n=int(input("Enter the number of elements:"))
for i in range (n):
    e=int(input('Enter the element into the list'))
    num.append(e)
    n=n-1
print("The maximum number is ",maximun(num,n) )         