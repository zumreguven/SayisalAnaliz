#Sayisal Analiz Dersi 2.Ödev 2.Soru

#x3+4x2-10=0 denkleminin [1,2] aralığındaki kökünü ikiye bölme metodu ile 4 iterasyonda gerçekleştiriniz.
x1=1  
x2=2
for i in range(4):
    x=(x1+x2)/2
    denklem=x**3 + x**2 - 10
    if denklem<0 :
        x1=x
    else:
        x2=x
print("ikiye bolme metodu ile bulunan kok ={}".format(x1))   