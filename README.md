# Doviz Kurlari

Türkiye Cumhuriyeti Merkez Bankası sitesinden XML olarak verileri alarak kullanmanızı sağlayacak Python kodu (nesnesi)'dir. 

Bilginin Alındığı Sayfa : www.tcmb.gov.tr -  http://www.tcmb.gov.tr/kurlar/today.xml


Kullanımı :
--------------------------

DovizKurlari.py dosyasını kodunuzun olduğu dizine ekleyin. 

Nesne'yi yarattıktan sonra DegerSor fonksiyonu ile değer alabilirsiniz. "DegerSor" fonksiyonu iki parametre alır. 

<b>DegerSor (<i>Parametre1, Parametre2</i>) </b>

<b>Parametre1 </b> = USD, EUR, AUD gibi para cinsinin resmi kısaltmaları 
<b>Parametre2 </b>= Almak istediğiniz değer ;

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

<code>
from DovizKur import DovizKurlari<br>
ornek = DovizKurlari()<br>
print ornek.DegerSor("EUR",4)<br>
Dolar_Deger = ornek.DegerSor("USD",4)<br>
print Dolar_Deger<br>
</code>
----------------------------------------------
