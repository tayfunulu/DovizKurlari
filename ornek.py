from DovizKurlari import DovizKurlari
ornek = DovizKurlari()
print ("Bugunun Kurlar : ")
print ("EURO DEGERI="+ornek.DegerSor("EUR",4))
Dolar_Deger = ornek.DegerSor("USD",4)
print ("DOLAR DEGERI="+Dolar_Deger)

print ("\nArsiv'deki bir degere bakalim. 10.02.2015")
print ("EURO DEGERI="+ornek.Arsiv("EUR",4,10,2,2015))
Dolar_Deger = ornek.Arsiv("USD",4,10,2,2015)
print ("DOLAR DEGERI="+Dolar_Deger)

print ("\nArsiv'deki bir degere bakalim. 27.03.2014")
print ("EURO DEGERI="+ornek.Arsiv_tarih("EUR",4,"27.03.2014"))
Dolar_Deger = ornek.Arsiv_tarih("USD",4,"27.03.2014")
print ("DOLAR DEGERI="+Dolar_Deger)
