import logging
import asyncio

from gino import Gino
from asyncpg.exceptions import UniqueViolationError

from ..db_gino import on_startup
from cooking_bot.config import Config
from .categories import Category
from .products import Product
from .dict_for_insert_in_db import DICT_FOR_INSERT_IN_DB


async def insert_obj_in_db(db: Gino, config: Config):
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
            elif sub == 'products':
                for product in DICT_FOR_INSERT_IN_DB[sub]:
                    ins = Product(**DICT_FOR_INSERT_IN_DB[sub][product])
                    await ins.create()
        logging.info('Данные вставлены в таблицы')
    except UniqueViolationError:
        logging.info('Таблица была заполнена ранее')
