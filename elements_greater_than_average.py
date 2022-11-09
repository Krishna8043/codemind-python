n=int(input())
l=list(map(int,input().split()))
l1=[]
s=sum(l)//len(l)
for i in l:
    if i>=s:
        l1.append(i)
print(len(l1))