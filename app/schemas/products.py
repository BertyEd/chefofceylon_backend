from typing import Union, List, Optional
from pydantic import BaseModel, Field
import datetime

from sqlalchemy import Float
from ..schemas.mixin import Mixing




class ProductOut(Mixing):
    product_name: str
    product_code: str
    description: str
    product_code: str
    regular_price: Union[float, None] = None
    discount_price: Union[float, None] = None
    stocks: int
    product_order: int
    product_image: Optional[str] = None
    # description: Union[str, None] = Field(
    #     default=None, title="The description of the item", max_length=300
    # )
    # price: float = Field(gt=0, description="The price must be greater than zero")
    # tax: Union[float, None] = None

    class Config:
        orm_mode = True



class AvailableDaysOut(Mixing):
    available_day : int
    product: ProductOut

    class Config:
        orm_mode = True
      

class WeekDayOut(Mixing):
    day : int
    day_product: List[AvailableDaysOut]

    class Config:
        orm_mode = True


class PostCodeOut(Mixing):
    post_code : str
    delivery_charge: float

    class Config:
        orm_mode = True



# shopping cart
class CartIn(BaseModel):
    quantity: int
    required_date: datetime.date
    product_code: str


class CartRemoveItem(BaseModel):
    required_date: str
    product_code: str










   
