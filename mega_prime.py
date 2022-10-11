def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True


n=int(input())
if prime(n)==True:
    s=str(n)
    c=0
    for i in s:
        if prime(int(i))==True:
            c+=1
            
    if c==len(s):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
    
    