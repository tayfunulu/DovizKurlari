# Doviz Kurlari

Türkiye Cumhuriyeti Merkez Bankası sitesinden XML olarak verileri alarak kullanmanızı sağlayacak Python kodu (nesnesi)'dir. 

Sayfa : www.tcmb.gov.tr -  http://www.tcmb.gov.tr/kurlar/today.xml

Kullanımı :

DovizKurlari.py dosyasını kodunuzun olduğu dizine ekleyin. 

Nesne'yi yarattıktan sonra DegerSor fonksiyonu ile değer alabilirsiniz. DegerSor fonksiyonu iki parametre alır. 

DegerSor (parametre1, parametre2) 

Parametre1 = USD, EUR, AUD gibi para cinsinin resmi kısaltmaları 
parametre2 = Almak istediğiniz değer 
[Kod,isim,CurrencyName,Unit,ForexBuying,ForexSelling,BanknoteBuying,BanknoteSelling,CrossRateUSD]
      0 : Kod kısaltmasını verir. 
      1 : Türkçe tanım . "ABD DOLARI" gibi. 
      2 : Yabancı tanım = CurrencyName 
      3 : Birim değeri = Genelde 1 olur. Bazı para cinsleri için 100'dür. 
      4 : Döviz Alış Değeri = Forex Buying 
      5 : Döviz Satış Değeri = Forex Selling
      6 : Efektif Alış Değeri = Banknote Buying
      7 : Efektif Satış Değeri = Banknote Selling 
      8 : Dolar ile çapraz parite 
      

Ornek Python Kodu :  
---------------------------------------------

from DovizKur import DovizKurlari

ornek = DovizKurlari()

print ornek.DegerSor("EUR",4)

Dolar_Deger = ornek.DegerSor("USD",4)

print Dolar_Deger

----------------------------------------------
