a=[]
c=0
for i in range(2,295245):
    for b in str(i):
        c+=int(b)**5
    if c==i:
        a.append(i)
    c=0
print(sum(a))    

        
    