import logging

from dotenv import load_dotenv
from vkwave.bots import SimpleLongPollBot, TaskManager


from cooking_bot.config import load_config
from cooking_bot.db_api.db_gino import db
from cooking_bot.db_api.models.categories import insert_cat_in_db

load_dotenv()

logger = logging.getLogger(__name__)


def main():
    '''Основная функция запуска бота.'''
    logging.basicConfig(
        level=logging.INFO,
        format=(
            u'%(filename)s:%(lineno)d: '
            u'#%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
        )
    )
    config = load_config()
    bot = SimpleLongPollBot(
        tokens=config.vk_bot.token,
        group_id=config.vk_bot.group_id
    )
    tm = TaskManager()
    tm.add_task(insert_cat_in_db(db, config))
    tm.add_task(bot.run())
    try:
        tm.run()
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped')
