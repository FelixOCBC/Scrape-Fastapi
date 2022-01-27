from pydantic import BaseModel
from typing import List


class BaseResponse(BaseModel):
    status: int = 200
    message: str = None
    data: List = []
    message2: str = None
    data2: List = []
    
class BaseResponse2(BaseModel):
    status: int = 200
    message2: str = None
    data2: List = []