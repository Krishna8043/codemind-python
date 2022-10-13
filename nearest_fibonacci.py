n=int(input())
a=0
b=1
c=0
l=[]
l1=[]
l2=[]
l.append(a)
l.append(b)
for i in range((n*2)):
    c=a+b
    l.append(c)
    a=b
    b=c
    c=0
for i in l:
    if i<n:
        l1.append(i)
    else:
        l2.append(i)
x=n-l1[-1] 
y=l2[0]-n

if x<y:
    print(l1[-1])
elif y<x:
    print(l2[0])
elif x==y:
    print(l1[-1],l2[0])