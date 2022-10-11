n=int(input())
m=n*n
s=str(n)
s1=s[::-1]
l=int(s1)*int(s1)
l2=str(l)
m1=l2[::-1]
if int(m1)==m:
    print(True)
else:
    print(False)
    