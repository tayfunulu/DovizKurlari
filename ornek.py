from DovizKurlari import DovizKurlari
ornek = DovizKurlari()
print ("Bugunun Kurlar : ")
print ("EURO DEGERI="+ornek.DegerSor("EUR",4))
Dolar_Deger = ornek.DegerSor("USD",4)
print ("DOLAR DEGERI="+Dolar_Deger)

print ("\nArsiv'deki bir degere bakalim.")
print ("EURO DEGERI="+ornek.Arsiv("EUR",4,10,02,2015))
Dolar_Deger = ornek.Arsiv("USD",4,10,02,2015)
print ("DOLAR DEGERI="+Dolar_Deger)
