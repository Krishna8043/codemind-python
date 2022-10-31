n=int(input())
l=list(map(int,input().split()))
es=0
for i in l:
    if i%2:
        es+=i
print(es)        