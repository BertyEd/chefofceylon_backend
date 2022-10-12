from ..models.models import Product
from fastapi.responses import JSONResponse
from fastapi import Request
from uuid import UUID, uuid4
#import requests



secret_key = 'cart'

class Cart(object):
    def __init__(self,request,db):

        session = uuid4()
        #data = SessionData(username='name')


        #self.session = requests.Session()
        self.session = request.session
        self.db = db
        cart = self.session.get(secret_key)

        if not cart:
            cart = self.session[secret_key] = {}

        self.cart = cart


    def add(self,product,required_date,quantity=1,required_time="5:00",update_quantity=False):
        product_code = str(product.product_code) + str(required_date)
        if product_code not in self.cart:
            self.cart[product_code] = {
                'product_id':str(product.id),
                'product_code':product.product_code,
                'product_name':product.product_name,
                'quantity':0,
                'discounted_price':str(product.price),
                'total_price':str(product.price * quantity),
                'required_time': required_time
                }

        if update_quantity:
            self.cart[product_code]['quantity']=quantity
        else:
            self.cart[product_code]['quantity'] += quantity


    def remove(self,product,required_date):
        product_code = str(product.product_code) + str(required_date)
        if product_code in self.cart:
            del self.cart[product_code]


    def remove_all(self):
        product_ids = list(self.cart.keys())
        for ids in product_ids:
            del self.cart[str(ids)]

    
    # def __iter__(self):
    #     product_ids = list(self.cart.keys())
    #     products = self.db.query(Product).filter(
    #         Product.product_code.in_(product_ids)
    #     ).all()

    #     cart = self.cart.copy()

    #     for product in products:
    #         cart[str(product.id)]['product'] = "" #jsonable_encoder(product)

    #     for item in cart.values():
    #         item['total_price'] = float(item['discounted_price']) * float(item['quantity'])

    #         yield item

    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    
    def get_total_price(self):
        return sum(float(item['discounted_price']) * float(item['quantity']) for item in self.cart.values())
