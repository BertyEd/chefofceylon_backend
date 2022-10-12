from fastapi import APIRouter,Depends,status
from ..models.models import Product,AvailableDays,WeekDays
from ..schemas.products import ProductOut, AvailableDaysOut, WeekDayOut
from typing import List
from ..database.db import get_db
from sqlalchemy.orm import Session



product_router = APIRouter(
    prefix='/products',
    tags=['products']
)


@product_router.get("/")
def index():
    return {'Hellow World..!'}



@product_router.get("/product_by_business_date/{business_date}/{week_day}",response_model=WeekDayOut)
def getProductByBussinessDays(business_date,week_day,db: Session = Depends(get_db)):   
    days = db.query(WeekDays).filter(WeekDays.day == week_day).first()
    #print(days)
    return days

