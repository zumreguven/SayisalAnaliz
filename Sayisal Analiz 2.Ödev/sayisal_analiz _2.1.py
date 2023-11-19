#Sayisal Analiz Dersi 2.Ödev 1.Soru


#1)x3-2x2-5=0 denkleminin [2,4] aralığındaki kökünü ikiye bölme metodu ile 4 iterasyonda gerçekleştiriniz.Bulunan çözümün kodunu yazınız
x1=2       #ilk aralık 2
x2=4       #ikinci aralık 4     
for i in range(4):
    x=(x1+x2)/2
    denklem= x**3 - 2*x**2 - 5
    if denklem<0:
        x1=x
        
    else:
        x2=x
    
print("ikili bölme sonucu bulunan kök ={}".format(x1))