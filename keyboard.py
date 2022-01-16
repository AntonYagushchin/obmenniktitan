from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

mailshot_btn = types.KeyboardButton('Сделать рассылку')
poll_btn = types.KeyboardButton('Сделать опрос', request_poll=types.KeyboardButtonPollType())
Keyboard_Start = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
Keyboard_Start.add(mailshot_btn)
Keyboard_Start.add(poll_btn)


gr_1 = InlineKeyboardButton("Заказчики", callback_data='gr1')
gr_2 = InlineKeyboardButton("Группа 2", callback_data='gr2')
gr_3 = InlineKeyboardButton("Группа 3", callback_data='gr3')
gr_4 = InlineKeyboardButton("Группа 4", callback_data='gr4')
Keyboard_Groups = InlineKeyboardMarkup(row_width=2)
Keyboard_Groups.add(gr_1, gr_2, gr_3, gr_4)


delete_key = InlineKeyboardButton("Удалить", callback_data='delete_message')
edit_key = InlineKeyboardButton("Редактировать", callback_data='edit_message')
Keyboard_message_edit = InlineKeyboardMarkup(row_width=2)
Keyboard_message_edit.add(edit_key, delete_key)

delete_key_poll = InlineKeyboardButton("Удалить", callback_data='delete_poll')
edit_key_poll = InlineKeyboardButton("Собрать аналитику", callback_data='analitycs_poll')
Keyboard_poll_edit = InlineKeyboardMarkup(row_width=2)
Keyboard_poll_edit.add(edit_key_poll, delete_key_poll)




