from fastapi import APIRouter,Depends,status
from ..models.models import Product,AvailableDays,WeekDays
from ..schemas.products import ProductOut, AvailableDaysOut, WeekDayOut, CartIn, CartRemoveItem
from typing import List
from ..database.db import get_db
from sqlalchemy.orm import Session
from fastapi import Request

from ..cart.cart import Cart


cart_router = APIRouter(
    prefix='/cart',
    tags=['cart']
)


@cart_router.get("/")
def index():
    return {'shopping cart'}


@cart_router.post("/add")
def add_to_cart(cart_request:CartIn,db:Session=Depends(get_db)):
    cart = Cart(cart_request,db)
    # product = db.query(Product).filter_by(product_code=cart_request.product_code,record_status=1).first()
    # cart.add(product,cart_request.required_date,cart_request.quantity,None,True)
    res = {'status':'success','cart':cart_request}
    return res


@cart_router.post("/remove")
def remove_cart_product(request:CartRemoveItem,db:Session=Depends(get_db)):
    cart = Cart(request,db)
    product = db.query(Product).filter_by(product_code=request.product_code,record_status=1).first()
    cart.remove(product,request.required_date)
    res = {'status':'success','cart':request}
    return res # should return new cart


@cart_router.get("/remove_all")
def remove_all_cart_items(request,db:Session=Depends(get_db)):
    cart = Cart(request,db)
    cart.remove_all()
    res = {'status':'success','cart':request} # should return new cart






