n=int(input())
l=list(map(int,input().split()))
dic={}
l1=[]
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if k==v:
        l1.append(k)
if len(l1)!=0 :
    print(min(l1),max(l1))
else:
    print(-1)