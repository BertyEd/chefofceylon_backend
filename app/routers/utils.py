from fastapi import APIRouter,Depends,status
from ..models.models import Product,AvailableDays,WeekDays, PostCode
from ..schemas.products import ProductOut, AvailableDaysOut, WeekDayOut, PostCodeOut
from typing import List
from ..database.db import get_db
from sqlalchemy.orm import Session



utill_router = APIRouter(
    prefix='/util',
    tags=['util']
)


@utill_router.get("/")
def index():
    return {'Utills'}



@utill_router.get("/postcodes",response_model=List[PostCodeOut])
def get_post_codes(db: Session = Depends(get_db)):   
    post_codes = db.query(PostCode).filter(PostCode.record_status == 1).order_by(PostCode.id).all()
    #print(days)
    return post_codes

    #,response_model=list(PostCodeOut)