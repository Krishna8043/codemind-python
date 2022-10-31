def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
                break
        else :
            return True
    else:
        return False

s=input()
n=int(s)

l=[]
for i in range(n,(n**2)):
    s2=str(i)
    s3=s2[::-1]
    if s2==s3 and isprime(i)==True:
        l.append(i)
for i in l:
    if i>n:
        print(i)
        break