from apps.models import Model
from . import db


class LoanFelix(Model):
    __table__ = 'datascrap'
    __primary_key__ = 'link'
    __timestamps__ = False

class Loan(Model):
    __table__ = 'neondataset2'
    __primary_key__ = 'idno'
    __timestamps__ = False
