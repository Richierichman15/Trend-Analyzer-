from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    product_id = Column(String, unique=True)
    product_name = Column(String)
    order_count = Column(Integer)
    price = Column(Float)
    review_count = Column(Integer)
    rating = Column(Float)
    timestamp = Column(DateTime)
    daily_order_velocity = Column(Integer)  # New: orders per day
    price_to_order_ratio = Column(Float)    # New: price/order relationship
