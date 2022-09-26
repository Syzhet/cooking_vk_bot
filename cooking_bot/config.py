from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv


@dataclass
class VkBot:
    token: str
    group_id: int
    host_id: int


@dataclass
class DbConfig:
    host: str
    database: str
    user: str
    password: str
    port: str


@dataclass
class Config:
    vk_bot: VkBot
    db: DbConfig


def load_config():
    '''Установка основных параметров для работы бота.'''
    load_dotenv()
    return Config(
        vk_bot=VkBot(
            token=getenv('BOT_TOKEN'),
            group_id=int(getenv('GROUP_ID')),
            host_id=int(getenv('HOST_ID')),
        ),
        db=DbConfig(
            host=getenv('DB_ID'),
            database=getenv('POSTGRES_DB'),
            user=getenv('POSTGRES_USER'),
            password=getenv('POSTGRES_PASSWORD'),
            port=getenv('DB_PORT')
        ),
    )
