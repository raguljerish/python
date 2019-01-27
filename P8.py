#raguljerish 
s=0
n=int(input("enter the value of N:"))
flag=0
for a in range (1,n+1):
    s=s+a
    flag=1
if flag==1:
    print ("the sum is",s)
else :    
    print ("invalid input")
    
