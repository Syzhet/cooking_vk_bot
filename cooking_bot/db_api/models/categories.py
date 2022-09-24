import logging
import asyncio

from sqlalchemy import Column, Integer, String, Text
from gino import Gino
from asyncpg.exceptions import UniqueViolationError

from ..db_gino import TimedBaseModel, on_startup
from cooking_bot.config import Config
from .inf_for_insert import DICT_FOR_INSERT_IN_DB


class Category(TimedBaseModel):
    __tablename__ = 'categories'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False, unique=True)
    description = Column(Text())
    image_uri = Column(String(200))


async def insert_cat_in_db(db: Gino, config: Config):
    engine = await on_startup(db, config)
    while not engine:
        await asyncio.sleep(0.1)
    logging.info('Вставляю данные в категории')
    try:
        for sub in DICT_FOR_INSERT_IN_DB:
            if sub == 'categories':
                for cat in DICT_FOR_INSERT_IN_DB[sub]:
                    ins = Category(**DICT_FOR_INSERT_IN_DB[sub][cat])
                    await ins.create()
        logging.info('Данные вставлены в таблицу categories')
    except UniqueViolationError:
        logging.info('Таблица была заполнена ранее')
