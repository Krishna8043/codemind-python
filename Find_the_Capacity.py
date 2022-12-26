s,t,b=map(int,input().split())
capacity=2*s*t*b*512
s=str(capacity//1024)
print(s+"KB")
