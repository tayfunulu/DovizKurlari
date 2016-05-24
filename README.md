# Doviz Kurlari

Türkiye Cumhuriyeti Merkez Bankası sitesinden XML olarak verileri alarak kullanmanızı sağlayacak Python kodu (nesnesi)'dir. 

Bilginin Alındığı Sayfa : www.tcmb.gov.tr -  http://www.tcmb.gov.tr/kurlar/today.xml


Kullanımı :
--------------------------

sistemden zip'li olarak çekin veya "git clone" ile direk sistemden clone yapın. 

<i><b>git clone https://github.com/tayfunulu/DovizKurlari.git</b>

cd DovizKurlari 

python ornek.py</i>

veya 

<i>python3 ornek.py</i>


Kendi kodunuzda kullanmak için DovizKurlari.py dosyasını kendi projenizin klasörünüze taşıyın. Sonrasında DovizKurları Nesnesi yaratarak, DegerSor fonksiyonu ile istediğiniz değeri sistemden çekebilirsiniz. "DegerSor" fonksiyonu iki parametre alır. 

<b>DegerSor (<i>Parametre1, Parametre2</i>) </b>

<b> Parametre1 </b> = USD, EUR, AUD gibi para cinsinin resmi kısaltmaları 

<b> Parametre2 </b>= Almak istediğiniz değer ;

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
