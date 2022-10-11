n=int(input())
l=[2,3,5]
for i  in l:
    while(n%i==0):
        n/=i
if n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")