a=float(input())
b=float(input())
c=float(input())
if((a+b)>c and (b+c)>a and (a+c)>b and a>0 and b>0 and c>0):
    if((a*a==b*b+c*c)or(b*b==c*c+a*a)or(c*c==a*a+b*b)):
        print("Tam giac vuong")
    if(a==b==c):
        print("Tam giac deu")
    if((a*a!=b*b+c*c)and(b*b!=c*c+a*a)and(c*c!=a*a+b*b)and a!=b!=c):
        print("Tam giac loai khac")
else:
    print("Khong hop le")