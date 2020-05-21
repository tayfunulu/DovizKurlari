# Doviz Kurlari Api Rest - Microservis - Docker

Türkiye Cumhuriyeti Merkez Bankası sitesinden XML olarak verileri alarak kullanmanızı sağlayacak Python kodu (nesnesi)'dir. Microservis olarak kullanmak içinde Dockerfile dosyası vardır. 

Eğitim ve bilgilendirme amaçlıdır. Ticari bir beklenti yoktur. 

Bilginin Alındığı Sayfa : www.tcmb.gov.tr -  http://www.tcmb.gov.tr/kurlar/today.xml

<hr>

<b>Örnek olması için Google Cloud'da örnek kod : </b>

https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz/usd

https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz/

https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz/2020/04/01

https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz/2020/04/01/eur

<hr>

<h1>Docker ile Kullanımı:</h1>

öncelikle docker hub'dan ilgili container image :

<code>docker pull tayfunulu/tl_doviz_kurlari</code>

Manual Çalıştırma (arka ekranda çalıştırma)

<code>docker run --rm -it -d -p 5000:5000 tayfunulu/tl_doviz_kurlari</code>

<hr>Docker-Compose dosyası 

    version: '3'
    services:
      doviz_microservis:
      container_name: tl_doviz_kurlari
      image: tayfunulu/tl_doviz_kurlari
      restart: always
      ports:
        - "5000:5000"

<hr>

Çalışıp çalışmadığını test edelim.

http://makinenin_ipsi:5000/api/doviz

<i>örnek</i>

http://127.0.0.1:5000/api/doviz

Çalışıyorsa aşağıdaki metotları kullanabilirsiniz.

<hr>

# RESTFUL-API KULLANIMI

<h2><b>/api/doviz</b></h2>

GET -> Güncel kur bilgilerinin tamamını verir. 

POST -> JSON ile tarih bilgisi gönderirseniz "gun.ay.yil" formatında "01.04.2020" ilgili günün tüm kurlarını verir. Hangi kuru istediğinizi eklerseniz sadece o kurun bilgileri gelir. 

            {"tarih":"01.04.2020"}  
            {"tarih":"01.04.2020","tur":"EUR"}  


<h2><b>/api/doviz/_TUR_</b></h2>

<i>örnek : /api/Doviz/USD</i> 

GET -> Seçilen Kur türünün tüm bilgilerini verir. 

POST -> Seçilen Kur türünün arşiv verisini almak için
    
            {"tarih":"01.04.2020"}  

<h2><b>/api/doviz/_yil/ay/gun_</b></h2>

<i>örnek : /api/doviz/2020/02/08</i>

GET -> Arşivden ilgili günün tüm kur bilgilerini verir. 

<h2><b>/api/doviz/_yil/ay/gun/TUR_</b></h2>

<i>örnek : /api/doviz/2020/02/010/USD</i>

GET -> Arşivden ilgili günün seçilen kur bilgilerini verir.             

<hr>

<b> Not : </b> Arşiv özelliğinde tatil günleri için Tatil günü olduğunu belirten bir hata döner


<hr>


<h1>Kendi Kodunuzda Nesne olarak Kullanımı :</h1>
--------------------------

sistemden zip'li olarak çekin veya "git clone" ile direk sistemden clone yapın. 

<i><b>git clone https://github.com/tayfunulu/DovizKurlari.git</b>

cd DovizKurlari 

<i>python3 ornek.py</i>


Kendi kodunuzda kullanmak için DovizKurlari.py dosyasını kendi projenizin klasörünüze taşıyın. Sonrasında DovizKurları Nesnesi yaratarak, DegerSor fonksiyonu ile istediğiniz değeri sistemden çekebilirsiniz. "DegerSor" fonksiyonu iki parametre alır. 

<code><b>DegerSor (<i>Parametre1, Parametre2</i>) </b></code>

<b>*</b> Parametre verilmezse JSON olarak tüm veriler döner 

<b> Parametre1 </b> = USD, EUR, AUD gibi para cinsinin resmi kısaltmaları 

<b> Parametre2 </b>= Almak istediğiniz değer ;

    "BanknoteBuying"    : Alış Değeri
    "BanknoteSelling"   : Satış Değeri
    "CrossRateUSD"      : USD ile çapraz kur
    "CurrencyName"      : Resmi Adı
    "ForexBuying"       : Forex Alış     
    "ForexSelling"      : Forex Satış
    "Kod"               : Kodu 
    "Unit"              : 1
    "isim"              : Türkçe Adı     

<b>Arşivden veri çekmek </b>

Eski bir tarihteki kur'u ögrenmek için Arsiv veya Arsiv_Tarih fonksiyonlarını kullanabilirsiniz.

<b>Arsiv (<i> Gun, Ay, Yil,Parametre1, Parametre2</i>) </b>

Gun, Ay, Yil = integer veya string olabilir. 


<b>Arsiv_Tarih (<i>Tarih,Parametre1, Parametre2</i>) </b>

Tarih = "01.02.2015" Şeklinde bir string veri olmalıdır. 

<hr>

<h1> Local'de Microservis olarak çalıştırılması. </h1>

<code> python3 flask_doviz_server.py</code>

Sonrasında 5000 portu dinlemeye başlar. Kullanımı yukarıda anlatıldığı gibidir. 
