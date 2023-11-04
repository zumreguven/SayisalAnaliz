import math
x=math.pi/5
x0=0
#taylor açılımı=  f(x)=f(x0) + f'(xo)*(x-x0) + (f''(x0)*(x-x0)'2)/2! + ...
f0=math.cos(x0)  #f0 değişkeni cos(0) ifadesine aktarılır.
fBirinciTurev=math.sin(x0) #fBirinciTurev değişkenine sin(0) sonucu atılır.
bulunanDeger=f0+fBirinciTurev*(x-x0)   
gercekDeger=math.cos(x) #cos(π/5) ifadesinin sonucu bulunur
print("bir terimli kesme hatası sonucu={}".format(gercekDeger-bulunanDeger)) #cos(π/5)den bulunan değer çıkarılarak 1.derecede kesme hatası bulunur
bulunanDeger2=bulunanDeger-(math.cos(x0)*(x**2)/2);
print("iki terimli kesme hatasi={}".format(gercekDeger-bulunanDeger2)) #cos(π/5)den bulunan değer çıkarılarak 2.derecede kesme hatası bulunur


