# Doviz Kurlari

Türkiye Cumhuriyeti Merkez Bankası sitesinden XML olarak verileri alarak kullanmanızı sağlayacak Python kodu (nesnesi)'dir. 

Sayfa : www.tcmb.gov.tr -  http://www.tcmb.gov.tr/kurlar/today.xml

Kullanımı :

DovizKurlari.py dosyasını kodunuzun olduğu dizine ekleyin. 

Sonra 
---------------------------------------------

from DovizKur import DovizKurlari

ornek = DovizKurlari()

print ornek.DegerSor("EUR",3)

Dolar_Deger = ornek.DegerSor("USD",3)

print Dolar_Deger

----------------------------------------------
