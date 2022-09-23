import logging

from typing import List
from datetime import datetime

from gino import Gino
import sqlalchemy as sa

from cooking_bot.config import Config


db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(
            f"{name}={value!r}" for name, value in values.items()
        )
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True

    created_at = db.Column(db.DateTime(True), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        server_default=db.func.now(),
    )


async def on_startup(db: Gino, config: Config):
    logging.info("Setup PostgreSQL Connection")
    username = config.db.user
    password = config.db.password
    db_name = config.db.database
    port = config.db.port
    uri = f'postgresql://{username}:{password}@localhost:{port}/{db_name}'
    await db.set_bind(uri)
    logging.info("PostgreSQL Connection - OK")
    logging.info('Create PostgreSQL tables')
    await db.gino.create_all()
    logging.info('Create PostgreSQL tables - OK')
