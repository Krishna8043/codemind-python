n=int(input())
l=[]
for i in range(n//3):
    l.append((i)*(i+1))
if n in l:
    print("YES")
else:
    print("NO")