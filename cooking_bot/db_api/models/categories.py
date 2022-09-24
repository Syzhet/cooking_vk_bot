from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from ..db_gino import TimedBaseModel


class Category(TimedBaseModel):
    __tablename__ = 'categories'

    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    description = Column(Text())
    photo_id = Column(String(200))
    products = relationship('Product', backref='category')
