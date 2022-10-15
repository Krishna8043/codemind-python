n=int(input())
s=abs(n)
s1=str(s)
x=s1[::-1]
if n%10==0 and n>0:
    print(x[1::])
elif n<0 and n%10==0:
    print("-"+x[1::])
elif n>0 and n%10!=0:
    print(x[0::])
else:
    print("-"+x[0::])
    