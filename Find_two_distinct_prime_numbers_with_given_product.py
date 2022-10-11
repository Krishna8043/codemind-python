def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True 
    
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0 and prime(i)==True:
        l.append(i)
if len(l)>=2:        
    print(*l)  
else:
    print(-1)