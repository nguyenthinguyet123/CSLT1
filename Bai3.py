print("Nhap hai canh ke cua tam giac vuong:")
a=int(input())
b=int(input())
import math
d=float(math.sqrt(a*a+b*b))
print("Canh ke thu nhat la: "+str(int(a))+", "+"canh ke thu hai la: "+str(int(b))+", "+"co canh huyen = "+"{0:.{1}f}".format(d,2))