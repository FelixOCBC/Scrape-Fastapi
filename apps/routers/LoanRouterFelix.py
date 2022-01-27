from datetime import date, datetime
from doctest import REPORT_UDIFF
import json
from urllib import response
from black import re
from fastapi import APIRouter, Body, FastAPI, Response
import fastapi
from apps.controllers.FelixController import ControllerFelix as loan


#qoutes = Scraper()
example_input_date = json.dumps({
    "tgl": "2022-01-26",
}, indent=2)

router = APIRouter()

@router.get("/{kategori}" ,description="Scrape the LINK & Title,kategori=(BERITA,NFT,BLOCKCHAIN,BITCOIN,ALTCOIN) Page = range page 1-(page)")
async def read_item(kategori: str,page:int):
    result = loan.getkategori(kategori,page)
    return result

@router.get("/detail/{kategori}",description="Scrape the detail,kategori=(BERITA,NFT,BLOCKCHAIN,BITCOIN,ALTCOIN) Page = range page 1-(page)")
async def read_item(kategori: str,page:int):
    result = loan.getdetail(kategori,page)
    return result

@router.get("/simpendata/{kategori}",description= "Scrape the LINK & Title,kategori=(BERITA,NFT,BLOCKCHAIN,BITCOIN,ALTCOIN) Page = range page 1-(page)")
async def save_item(kategori: str,page:int):
    result = loan.savedata(kategori,page)
    return result

@router.get("/getfromdb/{tgl}",description= "Take data from DB based on date, ex(2022-01-26)")
async def getdatafromdb(tgl: date):
    result = loan.getdatafromdb(tgl)
    return result