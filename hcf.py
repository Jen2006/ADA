#find the hcf 

#Division method


'''def hcf(a,b):

    while b!=0:
        a,b=b, a%b
    return a



a=int(input('Enter low number'))
b=int(input('Enter high number'))
print("The HCF is",hcf(a,b))'''

#JENSHI method

def hfc(a,b):
    l1=[]
    l2=[]
    c=[]

    for i in range(1,a+1):
        if a%i == 0:
           l1.append(i)
       

    for j in range(1,b+1):
        if b%j ==0:
            l2.append(j)    
        

    for x in l1:
        if x in l2:
            c.append(x)

    return max(c)     

a=int(input('Enter low number'))
b=int(input('Enter high number'))
print("The HCF is",hfc(a,b))  