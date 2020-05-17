#!/usr/bin/python
# -*- coding:utf-8 -*-
# Tayfun ULU
# 2016
# 2020 - Flask ile restful-api ekleme ve sadece python3'e dondurme

from flask import Flask, make_response, jsonify, request
import xml.etree.ElementTree as ET
import sys
from urllib.request import urlopen

class DovizKurlari():

	def __init__(self):
		pass

	def __veri_update(self,zaman="Bugun"):
		try :

			if zaman == "Bugun":
				self.url="http://www.tcmb.gov.tr/kurlar/today.xml"
			else:
				self.url=zaman

			tree = ET.parse(urlopen(self.url))
			
			root = tree.getroot()
			self.son={}
			self.Kur_Liste=[]
			i = 0 
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
				#self.son [Kod] = [Kod,isim,CurrencyName,Unit,ForexBuying,ForexSelling,BanknoteBuying,BanknoteSelling,CrossRateUSD]
				self.son [Kod] = { 
            "Kod":Kod,
            "isim":isim,
            "CurrencyName":CurrencyName,
            "Unit":Unit,
            "ForexBuying":ForexBuying,
            "ForexSelling":ForexSelling,
            "BanknoteBuying":BanknoteBuying,
            "BanknoteSelling":BanknoteSelling,
            "CrossRateUSD":CrossRateUSD
            }
          
			return self.son

		except :

			return "HATA"


	def DegerSor (self,*sor):
		self.__veri_update()
		if not(any(sor)):
				return self.son
		else:
				return self.son.get(sor[0]).get(sor[1])

	def Arsiv (self,Gun,Ay,Yil,*sor):
		a=self.__veri_update(self.__Url_Yap(Gun,Ay,Yil))
		if not(any(sor)):
			if a == "HATA":
				return {"Hata":"TATIL GUNU"}
			return self.son
		else :
			if a == "HATA":
				return "Tatil Gunu"
			else:
				return self.son.get(sor[0]).get(sor[1])

	def Arsiv_tarih (self,Tarih="",*sor):
		takvim = Tarih.split(".")
		Gun = takvim[0]
		Ay = takvim[1]
		Yil = takvim[2]
		a=self.__veri_update(self.__Url_Yap(Gun,Ay,Yil))
		if not(any(sor)):
			if a == "HATA":
				return {"Hata":"TATIL GUNU"}
			return self.son
		else :
			if a == "HATA":
				return "Tatil Gunu"
			else:
				return self.son.get(sor[0]).get(sor[1])

	def __Url_Yap (self,Gun,Ay,Yil):
		if len (str(Gun)) == 1 :
			Gun="0"+str(Gun)
		if len (str(Ay)) == 1 :
			Ay="0"+str(Ay)

		self.url = ("http://www.tcmb.gov.tr/kurlar/"+str(Yil)+str(Ay)+"/"+str(Gun)+str(Ay)+str(Yil)+".xml")
		return self.url

#Ornek Kullanım için
#from DovizKurlari import DovizKurlari
#ornek = DovizKurlari()
#print ornek.DegerSor("EUR",4)
