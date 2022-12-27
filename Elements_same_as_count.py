n=int(input())
l=list(map(int,input().split()))
s=set(l)
l1=[]
for i in l:
    a=l.count(i)
    if (a==i) and (i not in l1):
        l1.append(i)
if len(l1)!=0:
    print(*l1)
else:
    print(-1)