n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(len(l)):
    if i%2!=0 and l[i]%2!=0:
        l1.append(l[i])
    elif l[i]%2!=0:
        l2.append(l[i])
if(len(l2)==0):
    print("True")
else:
    print("False")