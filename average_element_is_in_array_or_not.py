n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
avg=int(s/len(l))
if avg in l:
    print(True)
else:
    print(False)