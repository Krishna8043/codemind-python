def prime_num(n):
    fc=0
    for i in range(1,n+1):
        n%i==0
        fc+=1
    if fc==0:
        return True
n=int(input())
a,b=0,0
if prime_num(n)==True:
    print(0)
else:
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
        print(abs(a-n))
    elif  abs(a-n)>abs(n-b):
        print(abs(n-b))
    else:
        print(abs(a-n))
    