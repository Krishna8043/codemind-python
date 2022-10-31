def prime(n):
    if n>1:
        for i in range(2,n):
             if n%i==0:
                 return False
                 break
        else:
            return True
    return False        
a=int(input())
l=[]
l1=[]
for i in range(1,a+1):
    if prime(i)==True:
        l.append(i)
    if a%i==0:
        l1.append(i)
for i in range(len(l)):
    if l[i] in l1:
        l1.remove(l[i])
print(len(l1))        
        