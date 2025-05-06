x = input("enter your number=")
x=int(x)
l=[]
for i in range(1,x+1):
    z=[]
    for b in range(1,i+1):
     z.append(i*b)
    l.append(z)  

print(l)  
