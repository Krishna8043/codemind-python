n=int(input())
sqr=n*n
c=0
l=[int(sqr) for sqr in str(sqr)]
c=sum(l)
if(n==c):
    print("Neon Number")
else:
    print("Not Neon Number")