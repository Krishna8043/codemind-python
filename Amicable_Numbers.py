n=int(input())
m=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
sum(l)
if sum(l)==m:
    print("Amicable")
else:
    print("Not Amicable")