def multiplylist(ml):
    result=1
    for x in ml:
        result=result*x
    return result    
n=int(input())
l=[int(n) for n in str(n)]
c=multiplylist(l)
if sum(l)==c:
    print("Spy Number")
else:
    print("Not Spy Number")