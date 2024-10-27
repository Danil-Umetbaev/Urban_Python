from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
API = ''
bot = Bot(token=API)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

@dispatcher.message_handler(commands='start')
async def start(message):
    print("Привет! Я бот, помогающий твоему здоровью.")

@dispatcher.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)