from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

API = ''
bot = Bot(token=API)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
@dispatcher.message_handler(commands='start')
async def start(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")

@dispatcher.message_handler(text='Calories')
async def set_age(message):
    await message.answer("Введите свой возраст: ")
    await UserState.age.set()

@dispatcher.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост: ")
    await UserState.growth.set()

@dispatcher.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=float(message.text))

    await message.answer("Введите свой вес: ")
    await UserState.weight.set()

@dispatcher.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=float(message.text))
    data = await state.get_data()

    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * (data['age']-1)
    await message.answer(f'Ваша норма калорий: {calories}.')
    await state.finish()
@dispatcher.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)