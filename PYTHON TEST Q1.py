a=int(input("enter n:"))
b=0
for i in range(1,a+1):
    if(not(i%2)==0):
        b+=i
print("sum of first n odd numbers :",b)
