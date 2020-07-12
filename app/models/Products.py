from datetime import datetime, date
from sqlalchemy.inspection import inspect
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, SmallInteger, Date, Float
from . import Base


class Products(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    sku = Column(String(30), nullable=True, unique=False)
    quantity = Column(Integer, nullable=True, unique=False)
    name = Column(String(100), nullable=True, unique=False)
    price = Column(Float, nullable=True, unique=False)
    cost_price = Column(Float, nullable=True, unique=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=True, unique=False)

    def __repr__(self):
        return f'<Product {self.id}>'
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
        