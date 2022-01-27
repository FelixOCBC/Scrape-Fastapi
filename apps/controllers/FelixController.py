from ast import Pass
from os import remove
from urllib import request
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.schema import Responsedate
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import LoanFelix
#from scraper import scrapedetaildata,scrapedata
from bs4 import BeautifulSoup
import requests
from datetime import date, datetime
import re

CLEANR = re.compile('<.*?>') 
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

SALT = PARAMS.SALT.salt


class ControllerFelix(object):
    @classmethod
    def getkategori(cls,kategori: str,hal: int):
        result = BaseResponse()
        result.status = 400
        qlist=[]
        for i in range(1,hal+1):
            url = f'https://blockchainmedia.id/category/{kategori}/page/' + str(i)
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
            }

            req = requests.get(url,headers=headers)
            soup = BeautifulSoup(req.content,'html.parser')


            items = soup.findAll('div','td-module-container td-category-pos-above')  
            for it in items:
                item = {
                'Link':it.find('div','td-module-thumb').find('a').get('href'),
                'Judul': it.find('h3','entry-title td-module-title').find('a').get_text() 
                }
                qlist.append(item)
        return qlist
        
    @classmethod
    def getdetail(cls,kategori:str,hal: int):
        result = BaseResponse()
        result.status = 400       
        detail=[]
        url2 = cls.getkategori(kategori,hal)      
        for i in range(len(url2)):
            url = url2[i]['Link']
            jud =  url2[i]['Judul']
            req = requests.get(url)
            soup = BeautifulSoup(req.text,'html.parser')            
            items = soup.findAll('div','tdc-content-wrap') 
            for it in items:
                date = it.find('time','entry-date updated td-module-date').get('datetime') 
                date_time_obj = datetime.strptime(str(date),'%Y-%m-%dT%H:%M:%S%z')
                date_time_obj = date_time_obj.replace(tzinfo=None)
                isi = it.find('div',attrs={'class':'tagdiv-type'})
                isi2 = isi.findAll('p')
                isi = cleanhtml(str(isi2))
                item = {
                'Judul':jud,
                'Link':url,
                'Author':it.find('a','tdb-author-name').get_text(),
                'Date':date_time_obj.strftime("%Y-%m-%d %H:%M:%S"),
                'isi':isi
                }
                
                detail.append(item)
        return detail
    
    @classmethod
    def savedata(cls,kategori: str,hal: int):

        result = BaseResponse()
        result.status = 400        
        good = []
        bad = []       
        input_data = cls.getdetail(kategori,hal)
        result.message2 ='Link Not Inputed'
        for i in range(len(input_data)):
            try:
                db = LoanFelix()
                db.judul = input_data[i]['Judul']
                db.link = input_data[i]['Link']
                db.author = input_data[i]['Author']
                db.tgl = input_data[i]['Date']
                db.isi = input_data[i]['isi']
                db.save()
                result.status = 200
                good.append(input_data[i]['Link'])
                result.message = "inputed"
                result.data = [good]
            except Exception as e:
                result.status = 404
                bad.append(input_data[i]['Link'])
                result.data2 = [bad]
                continue
            
            
        return result

    @classmethod
    def getdatafromdb(cls,tgl: date):
        input_data = tgl
        result = BaseResponse()
        result.status = 400
        try:
            if input_data is not None:
                data = LoanFelix.where('tgl','>=',input_data).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = Responsedate(**{"tgl": data})
                Log.info(result.message)
            else:
                e = "date not found"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result
