n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i==0 or i==1:
        l1.append(i)
    else:
        l2.append(i)
if len(l2)==0:
    print(True)
else:
    print(False)