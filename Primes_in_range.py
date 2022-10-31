from math import *
def isprime(n):
    if n>1:
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return False
                break
        else:
            return True
    else:
        return False
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if isprime(i)==True:
        c+=1
print(c)