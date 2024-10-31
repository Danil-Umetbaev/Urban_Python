from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API = ''
bot = Bot(token=API)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

text1 = ("АНТИБАГ! Самостоятельно находит и исправляет все баги, "
         "которые вы не заметили. Незаменимая вещь, когда уже слипаются глаза!")
text2 = "РУССКАЯ ДОКУМЕНТАЦИЯ! ТОЛЬКО ДЛЯ ВАС! Мы перевели всё на русский, читайте и наслаждайтесь!"
text3 = "БЕЗЛИМИТНЫЙ КОФЕ! Для самых самостоятельных и ответственных."
text4 = "Путёвка на МАЛЬДИВЫ! Когда ничего из вышеперечисленного не помогло..."

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
Reply_kb.add(btn1)
Reply_kb.add(btn2)
Reply_kb.add(btn3)

Inline_buy_kb = InlineKeyboardMarkup()
In_buy_btn1 = InlineKeyboardButton(text="Антибаг", callback_data="product_buying")
In_buy_btn2 = InlineKeyboardButton(text="Русская документация", callback_data="product_buying")
In_buy_btn3 = InlineKeyboardButton(text="Безлимитный кофе", callback_data="product_buying")
In_buy_btn4 = InlineKeyboardButton(text="Путёвка на мальдивы", callback_data="product_buying")
Inline_buy_kb.add(In_buy_btn1)
Inline_buy_kb.add(In_buy_btn2)
Inline_buy_kb.add(In_buy_btn3)
Inline_buy_kb.add(In_buy_btn4)
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
@dispatcher.message_handler(text="Купить")
async def get_buying_list(message):
    with open("images_products/antibag.png", 'rb') as img:
        await message.answer_photo(img, text1)
    with open("images_products/Russian documentation.png", 'rb') as img:
        await message.answer_photo(img, text2)
    with open("images_products/free coffee.png", 'rb') as img:
        await message.answer_photo(img, text3)
    with open("images_products/Maldivi.png", 'rb') as img:
        await message.answer_photo(img, text4)
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