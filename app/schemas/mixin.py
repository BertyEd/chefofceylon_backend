from tokenize import Number
from typing import Union,Optional
from pydantic import BaseModel, Field
import datetime



class Mixing(BaseModel):
    id: int
    created_at: datetime.datetime
    created_by: int
    modified_at: Optional[datetime.datetime] = None
    modified_by: Optional[int] = None
    record_status: int
   