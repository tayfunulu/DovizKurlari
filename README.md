# Güncellenmiyor 
<h3> microservice branch'ına bakın.  <br> 
 Python2 ile kullanmak isteyen olursa diye bunu master olarak bıraktım.</h3>

<hr>

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

<b>Arşivden veri çekmek </b>

Eski bir tarihteki kur'u ögrenmek için Arsiv veya Arsiv_Tarih fonksiyonlarını kullanabilirsiniz.

<b>Arsiv (<i>Parametre1, Parametre2, Gun, Ay, Yil</i>) </b>

Gun, Ay, Yil = integer veya string olabilir. 


<b>Arsiv_Tarih (<i>Parametre1, Parametre2, Tarih</i>) </b>

Tarih = "01.02.2015" Şeklinde bir string veri olmalıdır. 

Ornek Python Kodu :  
---------------------------------------------

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
