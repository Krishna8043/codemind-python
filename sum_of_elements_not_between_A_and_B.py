n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in l:
    if(i<a or i>b):
        sum+=i
print(sum)        