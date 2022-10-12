from sqlalchemy import Column,Integer, String,Boolean, ForeignKey, Text, DateTime , Float
from sqlalchemy.orm import relationship


from ..database.db import  Base
from .mixin import TimestampMixin


class User(Base,TimestampMixin):
    __tablename__ = "user"
    first_name = Column(String(50),nullable=False)
    last_name = Column(String(50))
    email = Column(String(100),nullable=False)
    password = Column(String(100),nullable=False)
    email_verified_at = Column(DateTime)
    is_confirm =  Column(Boolean,default=False,nullable=False)
    confirmation = Column(String(255))
    avatar_url = Column(Text())


class Product(Base,TimestampMixin):
    __tablename__ = "product"
    product_name = Column(String(100),nullable=False)
    description = Column(Text())
    product_code = Column(String(30),nullable=False)
    regular_price = Column(Float(asdecimal=2),nullable=False)
    discount_price = Column(Float(asdecimal=2),nullable=False)
    stocks =  Column(Integer,default=0,nullable=False)
    product_order =  Column(Integer,default=1,nullable=False) 
    product_image =  Column(String(100),nullable=False) 

    #sub_products = relationship("SubProduct", back_populates='product')
    available_days = relationship("AvailableDays", back_populates='product')


class SubProduct(Base,TimestampMixin):
    __tablename__ = "sub_product"
    subproduct_name = Column(String(100),nullable=False)   
    subproduct_description = Column(Text())
    product_code = Column(String(30), ForeignKey("product.product_code"))  # FK added
    
    # Relationships
    #product = relationship("Product",back_populates="sub_products")


class WeekDays(Base,TimestampMixin):
    __tablename__ = "week_days"
    day = Column(Integer,default=1,nullable=False)

    day_product = relationship("AvailableDays", back_populates='product_day')



class AvailableDays(Base,TimestampMixin):
    __tablename__ = "available_days"
    product_code = Column(String(30),ForeignKey("product.product_code"),nullable=False)
    available_day = Column(String(30),ForeignKey("week_days.day"),nullable=False)

    # Relationships
    product = relationship("Product",back_populates="available_days") 
    product_day = relationship("WeekDays",back_populates="day_product")


class PostCode(Base,TimestampMixin):
    __tablename__ = "post_codes"
    post_code = Column(String(30),nullable=False)
    delivery_charge = Column(Float(asdecimal=2),nullable=False)

    # Relationships
    # product = relationship("Product",back_populates="available_days") 
    # product_day = relationship("WeekDays",back_populates="day_product")



class Cart(Base,TimestampMixin):
    __tablename__ = "cart"
    pass



    
    



