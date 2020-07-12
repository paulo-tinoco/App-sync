from datetime import datetime, date
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, SmallInteger, Date, Float
from . import Base


class Orders(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    status = Column(String(50), nullable=True, unique=False, default=date.today)
    date = Column(Date, nullable=True, unique=False, default=date.today)
    partial_total = Column(Float, nullable=True, unique=False)
    discount = Column(Float, nullable=True, unique=False)
    point_sale = Column(String(100), nullable=True, unique=False)
    shipment_value = Column(Float, nullable=True, unique=False)
    total = Column(Float, nullable=True, unique=False)
    modified = Column(DateTime, nullable=False, unique=False, default=datetime.now, onupdate=datetime.now)
    products = relationship('Products', backref='orders')

    def __repr__(self):
        return f'<Order {self.id}>'
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
        