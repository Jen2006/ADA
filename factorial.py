# find the factorial using recursion

def fact(n):
    if n<=1:
        return 1
    
    else:
        return n * fact(n-1)
    
n=int(input("Enter a number"))

print(f"The factorial of {n} is :", fact(n))


#Algorithm
'''
s1:Start
s2:Enter a number
s3:Set Base condition  
     if n<=1 return 1
   Else return n*factorial(n-1)

s4:print output
s5:stop


'''