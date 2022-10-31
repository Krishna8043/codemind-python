def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
n1=int(input())
n2=int(input())
for i in range(n1,n2):
    if prime(i)==True:
        print(i)
        
                