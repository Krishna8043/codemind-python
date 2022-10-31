n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if l[i]%2==0:
        l1.append(i)
print(l1[-1])