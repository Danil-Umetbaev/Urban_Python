from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from crud_function import *

API = ''
bot = Bot(token=API)
dispatcher = Dispatcher(bot, storage=MemoryStorage())



Inline_kb = InlineKeyboardMarkup()
In_btn1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
In_btn2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
In_btn3 = InlineKeyboardButton(text="Не в этот раз", callback_data="close")
Inline_kb.add(In_btn1)
Inline_kb.add(In_btn2)
Inline_kb.add(In_btn3)

Reply_kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="Рассчитать")
btn2 = KeyboardButton(text="Информация")
btn3 = KeyboardButton(text="Купить")
btn4 = KeyboardButton(text="Регистрация")
Reply_kb.add(btn1)
Reply_kb.add(btn2)
Reply_kb.add(btn3)
Reply_kb.add(btn4)

Inline_buy_kb = InlineKeyboardMarkup()
In_buy_btn1 = InlineKeyboardButton(text="Антибаг", callback_data="product_buying")
In_buy_btn2 = InlineKeyboardButton(text="Русская документация", callback_data="product_buying")
In_buy_btn3 = InlineKeyboardButton(text="Безлимитный кофе", callback_data="product_buying")
In_buy_btn4 = InlineKeyboardButton(text="Путёвка на мальдивы", callback_data="product_buying")
Inline_buy_kb.add(In_buy_btn1)
Inline_buy_kb.add(In_buy_btn2)
Inline_buy_kb.add(In_buy_btn3)
Inline_buy_kb.add(In_buy_btn4)

products = get_all_product()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

@dispatcher.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer(text="Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dispatcher.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if not(is_included(username)):
        await state.update_data(username=username)
        await message.answer(text="Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Вы уже зарегестрированы.")
        await state.finish()

@dispatcher.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer(text="Введите свой возраст:")
    await RegistrationState.age.set()

@dispatcher.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer("Вы успешно зарегистрировались!")
    await state.finish()


@dispatcher.message_handler(text="Купить")
async def get_buying_list(message):

    with open("images_products/antibag.png", 'rb') as img:
        product_1 = f'Название: {products[0][1]} / Описание: {products[0][2]} / Цена: {products[0][3]}.'
        await message.answer_photo(img, product_1)
    with open("images_products/Russian documentation.png", 'rb') as img:
        product_2 = f'Название: {products[1][1]} / Описание: {products[1][2]} / Цена: {products[1][3]}.'
        await message.answer_photo(img, product_2)
    with open("images_products/free coffee.png", 'rb') as img:
        product_3 = f'Название: {products[2][1]} / Описание: {products[2][2]} / Цена: {products[2][3]}.'
        await message.answer_photo(img, product_3)
    with open("images_products/Maldivi.png", 'rb') as img:
        product_4 = f'Название: {products[3][1]} / Описание: {products[3][2]} / Цена: {products[3][3]}.'
        await message.answer_photo(img, product_4)
    await message.answer("Какой продукт желаете приобрести?", reply_markup=Inline_buy_kb)

@dispatcher.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()
@dispatcher.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer(text="Выберите опцию:", reply_markup=Inline_kb)

@dispatcher.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("""для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
    для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.""")
    await call.answer()

@dispatcher.callback_query_handler(text="close")
async def get_formulas(call):
    await call.message.answer("Приходите ещё!")
    await call.answer()

@dispatcher.message_handler(commands='start')
async def start(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=Reply_kb)

@dispatcher.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст: ")
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
    await message.answer(text="Выберите опцию:", reply_markup=Inline_kb)

@dispatcher.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)