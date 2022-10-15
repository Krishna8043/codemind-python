n=input()
l=[]
for i in n:
    if i not in l:
        l.append(i)
    elif i in l:
        print("Not Unique Number")
        break
else:
    print("Unique Number")