def digit(s):
    s1=0
    while(s!=0):
        r=s%10
        s1=(r**2)+s1
        s=s//10
    return s1
n=int(input())
if n==1 or n==7:
    print("True")
else:
    while(n>=9):
        n=digit(n)
        #print(n)
        if n==1 or n==7:
            print("True")
            break
    else:
        print("False")