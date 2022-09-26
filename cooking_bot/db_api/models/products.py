from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, String, Text

from ..db_gino import TimedBaseModel


class Product(TimedBaseModel):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    description = Column(Text())
    photo_id = Column(String(200))
    photo_url = Column(String(200))
    category_id = Column(SmallInteger(), ForeignKey('categories.id'))
