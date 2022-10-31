n=int(input())
l=list(map(int,input().split()))
c=int(input())
z=0
if c in l:
    for i in l:
        if i==c:
            z+=1
    print(z)
else:
    print(0)
    