n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l),1):
    j=i+2
    if j<n:
        if ((l[i]%2)==0 and (l[j]%2!=0)):
            c+=1
        elif ((l[i]%2) and (l[j]%2)==0):
            c+=1
print(c)