import datetime
from sqlite3 import Timestamp
from datetime import date, datetime
from numpy import datetime_data
from pydantic import BaseModel
from typing import Optional, List

class RequestDate(BaseModel):
    tgl: datetime = None


class borrowbase(BaseModel):

    judul: str = None
    link: str = None
    author: str = None
    tgl: date = None
    isi: str = None


class Responsedate(BaseModel):   
    tgl: List[borrowbase]

