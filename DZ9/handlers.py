from loader import dp, bot
from aiogram import types


# @dp.message_handler()
# async def mes_all(message: types.Message):
#     global total
#     if message.text.isdigit():
#         total -= int(message.text)
#         await bot.send_message(message.from_user.id, f'Конфет на столе осталось - {total}')
#         await message.answer(f'Гляди, что поймал {message.text}')
#     else: 
#         await bot.send_message(message.from_user.id, f'Введите число')

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
        print(message)
        await message.answer(f'Привет {message.from_user.first_name}! Давненько тебя не видел')

# @dp.message_handler(text=['лох'])
# async def mes_loh(message: types.Message):
#         await bot.delete_message(message.from_user.id, message.message_id)
#         await message.answer('Так у нас говорить нельзя')

# @dp.message_handler(commands=['set'])
# async def mes_set(message: types.Message):
#         global total 
#         count = message.text.split()[1]
#         total = int(count)
#         await message.answer(f"Установили новое колличество конфет в размере {total}")
   

# @dp.message_handler()
# async def mes_oop(message: types.Message):
#     await message.answer(f'Гляди, что поймал {message.text}')

    