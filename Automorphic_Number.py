n=int(input())
s=str(n)
m=n**2
s1=str(m)
s2=s1[::-1]
x=""
c=0
for i in range(len(s)):
    r=n%10
    c+=1
    n=n//10

x=(s2[0:c:1])
if (x[::-1]) == s:
    print("Automorphic Number")
else :
    print("Not an Automorphic Number")