n=int(input())
l=list(map(int,input().split()))
s=set(l)
l1=[]
for i in s:
    a=l.count(i)
    if(a==i):
        l1.append(i)
if len(l1)!=0:
    avg=(sum(l1)/len(l1))
    print("%0.2f"%avg)
else:
    print(-1)