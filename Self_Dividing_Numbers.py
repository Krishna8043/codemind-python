m=int(input())
n=int(input())
l=[]
l1=[]
for i in range (m,n+1):
    if i<=9:
        l.append(i)
    elif(i>=10 and i%10!=0):
        s=str(i)
        count=0
        for j in s:
            if i%(int(j))==0:
                count=count+1
        if(count==int(len(s))):
            l.append(i)
print(*l)  