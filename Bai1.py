a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
p=float((a+b+c)/2)
if((a+b)>c and (b+c)>a and (a+c)>b):
    import math
    s=float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    print("Dien tich="+str(round(s,3)))
else:
    print("Khong hop le")