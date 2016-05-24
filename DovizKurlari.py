#!/usr/bin/python
# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import urllib2

class DovizKurlari():

    def __init__(self):
        self.__veri_update()

    def __veri_update(self):
        tree = ET.parse(urllib2.urlopen('http://www.tcmb.gov.tr/kurlar/today.xml'))
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

    def DegerSor (self,sor,sor2):
            return self.son[sor][sor2]

#Ornek Kullanım için
#from DovizKur import DovizKurlari
#ornek = DovizKur()
#print ornek.DegerSor("EUR",4)
