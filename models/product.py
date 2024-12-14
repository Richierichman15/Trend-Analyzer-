from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    product_id = Column(String)
    product_name = Column(String)
    order_count = Column(Integer)
    price = Column(Float)
    review_count = Column(Integer)
    rating = Column(Float)
    timestamp = Column(DateTime)  
    daily_order_velocity = Column(Integer)
    price_to_order_ratio = Column(Float)


engine = create_engine("sqlite:///./products.db")
Base.metadata.create_all(engine)