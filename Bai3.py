x=float(input("x="))
y=float(input("y="))
ch=input("Phep toan:")
a=float(x+y)
b=float(x-y)
c=float(x*y)
d=float(x/y)
if(ch=="+"):
    print(str(x)+"+"+str(y)+"="+str(a))
if(ch=="-"):
    print(str(x)+"-"+str(y)+"="+str(b))
if(ch=="*"):
    print(str(x)+"*"+str(y)+"="+str(round(c,1)))
if(ch=="/"):
    print(str(x)+"/"+str(y)+"="+str(round(d,1)))
if(ch=="/" and y==0):
    print("Khong hop le")
if(ch!="+"and ch!="-" and ch!="*" and ch!="/"):
    print("Khong hop le")