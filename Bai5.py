n=int(input("So tien ban dau: "))
k=int(input("So thang gui: "))
t=float(input("Lai suat/ thang: "))
m=float(n*(1+k*t))
print("Voi so tien ban dau "+str(n)+", sau "+str(k)+" thang gui, lai suat "+str(t)+"/ thang")
print("Thi so tien nhan duoc cuoi ky la: "+"{0:.{1}f}".format(m,1))