#!/usr/bin/python
# -*- coding:utf-8 -*-
# Tayfun ULU
# 2016

import xml.etree.ElementTree as ET
import sys
if sys.version_info.major >2 :
	from urllib.request import urlopen
else :
	import urllib2

class DovizKurlari():

	def __init__(self):
        	pass

	def __veri_update(self,zaman="Bugun"):
		try :

			if zaman == "Bugun":
				self.url="http://www.tcmb.gov.tr/kurlar/today.xml"
			else:
				self.url=zaman

			if sys.version_info.major >2 :
				tree = ET.parse(urlopen(self.url))
			else :
				tree = ET.parse(urllib2.urlopen(self.url))


			root = tree.getroot()
			self.son={}
			self.Kur_Liste=[]

			for kurlars in root.findall('Currency'):
				Kod= kurlars.get('Kod')
				Unit = kurlars.find('Unit').text #    <Unit>1</Unit>
				isim = kurlars.find('Isim').text #    <Isim>ABD DOLARI</Isim>
				CurrencyName = kurlars.find('CurrencyName').text #    <CurrencyName>US DOLLAR</CurrencyName>
				ForexBuying = kurlars.find('ForexBuying').text #    <ForexBuying>2.9587</ForexBuying>
				ForexSelling = kurlars.find('ForexSelling').text #    <ForexSelling>2.964</ForexSelling>
				BanknoteBuying = kurlars.find('BanknoteBuying').text #    <BanknoteBuying>2.9566</BanknoteBuying>
				BanknoteSelling = kurlars.find('BanknoteSelling').text #    <BanknoteSelling>2.9684</BanknoteSelling>
				CrossRateUSD = kurlars.find('CrossRateUSD').text #    <CrossRateUSD>1</CrossRateUSD>
				self.Kur_Liste.append(Kod)
				self.son [Kod] = [Kod,isim,CurrencyName,ForexBuying,ForexSelling,BanknoteBuying,BanknoteSelling,CrossRateUSD]

			return self.son

		except :

			return "HATA"



	def DegerSor (self,sor,sor2):
		self.__veri_update()
		return self.son[sor][sor2]

	def Arsiv (self,sor,sor2,Gun,Ay,Yil):
		a=self.__veri_update(self.__Url_Yap(Gun,Ay,Yil))
		if a == "HATA":
			return "TATIL GUNU"
		else:
			return self.son[sor][sor2]

	def Arsiv_tarih (self,sor,sor2,Tarih):
		takvim = Tarih.split(".")
		Gun = takvim[0]
		Ay = takvim[1]
		Yil = takvim[2]
		a=self.__veri_update(self.__Url_Yap(Gun,Ay,Yil))
		if a == "HATA":
			return "TATIL GUNU"
		else :
			return self.son[sor][sor2]

	def __Url_Yap (self,Gun,Ay,Yil):
		if len (str(Gun)) == 1 :
			Gun="0"+str(Gun)
		if len (str(Ay)) == 1 :
			Ay="0"+str(Ay)

		self.url = ("http://www.tcmb.gov.tr/kurlar/"+str(Yil)+str(Ay)+"/"+str(Gun)+str(Ay)+str(Yil)+".xml")
		return self.url

#Ornek Kullanım için
#from DovizKur import DovizKurlari
#ornek = DovizKur()
#print ornek.DegerSor("EUR",4)
