import os
from turtle import xcor
from fastapi import FastAPI,Depends,status
from .database.db import engine, Base, init_db
from .models import models
import datetime
from datetime import date
from .routers.products import product_router
from .routers.cart import cart_router
from .routers.utils import utill_router
from fastapi.responses import FileResponse ,HTMLResponse

from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware








origins = [
    # "http://localhost.5173",
    # "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

middlewares = [
    Middleware(SessionMiddleware,secret_key='cart'),
    Middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

]

app = FastAPI(middleware=middlewares)


# add routers #############################################
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(utill_router)



# start up methods ######################################
@app.on_event("startup")
async def startup_event():
    init_db(app)


#routes ####################################################
@app.get("/")
def index():
    return HTMLResponse('<h1>ChefOfCeylon API<h1>')



@app.get("/bussines_days")
def index():
    today = date.today()
    bussines_days = []   
    for x in range(15):
        today = today + datetime.timedelta(days=1)
        week_day = today.isoweekday()
        if week_day>=1 and week_day<=5:
            data_dict = {
                'date':today,
                'week_day':week_day,
                'ordered_qty':0
            }
            bussines_days.append(data_dict)
    return bussines_days


@app.get("/images/{image_name}")
async def view_image(image_name):
    image_with_path = f"app/images/{image_name}" 
    return FileResponse(image_with_path)
    