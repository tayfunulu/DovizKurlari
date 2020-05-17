#!/usr/bin/python

from DovizKurlari import DovizKurlari
# ornek isimli nesne yaratiliyor. 
ornek = DovizKurlari()
print ("Bugunun Kurlar : ")
print ("EURO DEGERI="+ornek.DegerSor("EUR","ForexBuying"))
# deger sor fonksiyonu ile USD'nin degeri sorgulaniyor. 
Dolar_Deger = ornek.DegerSor("USD","ForexBuying")
print ("DOLAR DEGERI="+Dolar_Deger)

# Arsiv konusu
print ("\nArsiv'deki bir degere bakalim. 02.02.2015")
print ("EURO DEGERI="+ornek.Arsiv(2,2,2015,"EUR","ForexBuying"))
# 02.02.2015 tarihindeki USD'in degeri sorgulaniyor. 
Dolar_Deger = ornek.Arsiv(2,2,2015,"USD","ForexBuying")
print ("DOLAR DEGERI="+Dolar_Deger)

print ("\nArsiv'deki bir degere bakalim. 10.02.2015")
print ("EURO DEGERI="+ornek.Arsiv_tarih("10.02.2015","USD","ForexBuying"))
Dolar_Deger = ornek.Arsiv_tarih("10.02.2015","USD","ForexBuying")
print ("DOLAR DEGERI="+Dolar_Deger)

print ("\nArsiv'deki bir degere bakalim ve hata verdigini gorelim. 01.02.2015")
print ("EURO DEGERI="+ornek.Arsiv_tarih("01.02.2015","EUR","ForexBuying"))
Dolar_Deger = ornek.Arsiv_tarih("01.02.2015","EUR","ForexBuying")
print ("DOLAR DEGERI="+Dolar_Deger)
