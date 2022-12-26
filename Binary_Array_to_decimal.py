n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
s=0
for i in range(len(l)):
    if l1[i]==1:
        s=s+2**i
    else:
        continue
print(s)    