t=int(input())
for i in range(t):
    n=int(input())
    a,b=0,0
    for i in range(n,n*n):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            a=i
            break
    for i in range(n-1,0,-1):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            b=i
            break
    if  abs(a-n)<abs(n-b):
        print(a)
    elif  abs(a-n)>abs(n-b):
        print(b)
    elif abs(a-n)==abs(n-b):
        print(b)
    