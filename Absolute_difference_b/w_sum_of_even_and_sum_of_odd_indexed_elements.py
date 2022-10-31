n=int(input())
l=list(map(int,input().split()))
es=0
os=0
for i in range(len(l)):
    if i%2==0:
        es+=l[i]
    elif i%2!=0:
        os+=l[i]
        
sum=abs(es-os)
print(sum)