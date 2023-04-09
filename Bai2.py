a=int(input("M1="))
b=int(input("M2="))
c=int(input("M3="))
s=int(input("S="))
if(1<=s<=100):
    m=int(s*a)
elif(101<=s<=150):
    m=int(100*a+(s-100)*b)
else:
    m=int(100*a+50*b+(s-150)*c)
print("Phai tra="+str(m))