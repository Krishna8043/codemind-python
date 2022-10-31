n=int(input())
l=list(map(int,input().split()))
es=0
os=0
for i in l:
    if i%2==0:
        es+=i
    elif i%2!=0:
        os+=i
sum=abs(es-os)
print(sum)
    