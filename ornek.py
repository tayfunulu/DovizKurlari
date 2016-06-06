from DovizKurlari import DovizKurlari
# ornek isimli nesne yaratiliyor. 
ornek = DovizKurlari()
print ("Bugunun Kurlar : ")
print ("EURO DEGERI="+ornek.DegerSor("EUR",4))
# deger sor fonksiyonu ile USD'nin degeri sorgulaniyor. 
Dolar_Deger = ornek.DegerSor("USD",4)
print ("DOLAR DEGERI="+Dolar_Deger)

# Arsiv konusu
print ("\nArsiv'deki bir degere bakalim. 02.02.2015")
print ("EURO DEGERI="+ornek.Arsiv("EUR",4,2,2,2015))
# 02.02.2015 tarihindeki USD'in degeri sorgulaniyor. 
Dolar_Deger = ornek.Arsiv("USD",4,2,2,2015)
print ("DOLAR DEGERI="+Dolar_Deger)

print ("\nArsiv'deki bir degere bakalim. 10.02.2015")
print ("EURO DEGERI="+ornek.Arsiv_tarih("EUR",4,"10.02.2015"))
Dolar_Deger = ornek.Arsiv_tarih("USD",4,"10.02.2015")
print ("DOLAR DEGERI="+Dolar_Deger)

print ("\nArsiv'deki bir degere bakalim ve hata verdigini gorelim. 01.02.2015")
print ("EURO DEGERI="+ornek.Arsiv_tarih("EUR",4,"01.02.2015"))
Dolar_Deger = ornek.Arsiv_tarih("USD",4,"01.02.2015")
print ("DOLAR DEGERI="+Dolar_Deger)
