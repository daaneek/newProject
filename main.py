import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from bot.config import Config
from bot.commands import register_commands
from bot.updatesworker import get_handled_updates_list

async def set_commands(bot: Bot):
    """ Команды """
    commands = [
        BotCommand(command="/start", description="Начать"),
        BotCommand(command="/help", description="Помочь"),
        BotCommand(command="/pravila", description="Правила")
        ]
    await bot.set_my_commands(commands)



logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",)

    config: Config = Config()

    bot = Bot(config.token, parse_mode="HTML")
    dp = Dispatcher(bot)
    
    # Базовый функционал
    register_commands(dp)
    
    # Установка команд бота при старте
    await set_commands(bot) 
    try:
        await dp.start_polling(allowed_updates=get_handled_updates_list(dp))
    finally:
        await bot.session.close()


if __name__=='__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Exit")

