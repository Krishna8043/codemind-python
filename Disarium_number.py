n=int(input())
s=str(n)
s1=0
for i in range(len(s)):
    s1+=(int(s[i])**(i+1))
if s1==n:
    print(True)
else:
    print(False)
    