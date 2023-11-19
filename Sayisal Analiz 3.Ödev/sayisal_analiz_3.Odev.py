#f(x)=4(e^-0.5x)-x denkleminin kökünü Newton-raphson ile başlangıç değeri x0=2 alarak 4 iterasyon sonucunda bulunuz.
import math
x=2
for i in range(4):
    a=(-2*math.e**(-0.5*x))-1
    denklem=( 4 *math.e**(-0.5*x))-x
    b=x-(denklem/a)
    x=b
print("Newton-raphson sonucu= {}".format(x))