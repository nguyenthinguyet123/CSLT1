r=int(input("Nhap vao ban kinh của duong tron: "))
pi=3.14
s=float(pi*r*r)
c=float(2*r*pi)

print("Dien tich cua duong tron co ban kinh "+str(int(r))+" la = "+"{0:.{1}f}".format(s,1))
print("Chu vi cua duong tron co ban kinh "+str(int(r))+" la = "+"{0:.{1}f}".format(c,1))