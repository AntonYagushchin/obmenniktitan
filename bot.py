import logging
import time

logging.basicConfig(level=logging.INFO)
from quizzer import Poll
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from config import BOT_ADMIN1, BOT_ADMIN2, BOT_DEV, RECOVER_ID
import keyboard
import base_worker as DB
import config

group_1_path = "Base\\Group1.txt"
group_2_path = "Base\\Group2.txt"
group_3_path = "Base\\Group3.txt"
group_4_path = "Base\\Group4.txt"

# ----------init-----------
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# ----------init-----------


# ---------main code--------

async def return_state():

    config.MAILSHOT_FLAG = False

    config.POLL_FLAG = False

    config.SOLO_ADD1 = False
    config.SOLO_ADD2 = False
    config.SOLO_ADD3 = False
    config.SOLO_ADD4 = False

    config.GR1 = False
    config.GR2 = False
    config.GR3 = False
    config.GR4 = False

    config.DELETING1 = False
    config.DELETING2 = False
    config.DELETING3 = False
    config.DELETING4 = False

    config.CATCH_MSG_GR1 = False
    config.CATCH_MSG_GR2 = False
    config.CATCH_MSG_GR3 = False
    config.CATCH_MSG_GR4 = False

    config.EDITING = False


async def process_callback_button1(msg: types.Message):
    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await bot.send_message(msg.from_user.id, 'Выберите группу для отпрвавки рассылки',
                               reply_markup=keyboard.Keyboard_Groups)
        await process_getall()
        print(config.MAILSHOT_FLAG)

    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять текст в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить рассылку\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))


async def process_getall():
    await bot.send_message(RECOVER_ID, DB.getAll(), parse_mode="Markdown")


@dp.message_handler(commands=['get_base'])
async def process_get_base(msg: types.Message):
    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:

        time.sleep(2)
        await bot.send_message(msg.from_user.id, DB.getAll(), parse_mode="Markdown")
        await process_getall()

@dp.message_handler(commands=['poll_manager_gr1'])
async def managing_process1(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Последний отправленый опрос:")
        await bot.send_poll(chat_id=msg.from_user.id,
                            question=config.LAST_POLL_GR1.Poll.question,
                            options=config.LAST_POLL_GR1.Poll.options,
                            type=config.LAST_POLL_GR1.Poll.type,
                            correct_option_id=config.LAST_POLL_GR1.Poll.correct_option_id,
                            is_anonymous=config.LAST_POLL_GR1.Poll.is_anonymous,
                            allows_multiple_answers=config.LAST_POLL_GR1.Poll.allows_multiple_answers)
        await bot.send_message(msg.from_user.id, "Выберите действие:", reply_markup=keyboard.Keyboard_poll_edit)
        config.GR1 = True
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))

@dp.message_handler(commands=['poll_manager_gr2'])
async def managing_process2(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Последний отправленый опрос:")
        await bot.send_poll(chat_id=msg.from_user.id,
                            question=config.LAST_POLL_GR2.Poll.question,
                            options=config.LAST_POLL_GR2.Poll.options,
                            type=config.LAST_POLL_GR2.Poll.type,
                            correct_option_id=config.LAST_POLL_GR2.Poll.correct_option_id,
                            is_anonymous=config.LAST_POLL_GR2.Poll.is_anonymous,
                            allows_multiple_answers=config.LAST_POLL_GR2.Poll.allows_multiple_answers)
        await bot.send_message(msg.from_user.id, "Выберите действие:", reply_markup=keyboard.Keyboard_poll_edit)
        config.GR2 = True
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))

@dp.message_handler(commands=['poll_manager_gr3'])
async def managing_process1(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Последний отправленый опрос:")
        await bot.send_poll(chat_id=msg.from_user.id,
                            question=config.LAST_POLL_GR3.Poll.question,
                            options=config.LAST_POLL_GR3.Poll.options,
                            type=config.LAST_POLL_GR3.Poll.type,
                            correct_option_id=config.LAST_POLL_GR3.Poll.correct_option_id,
                            is_anonymous=config.LAST_POLL_GR3.Poll.is_anonymous,
                            allows_multiple_answers=config.LAST_POLL_GR3.Poll.allows_multiple_answers)
        await bot.send_message(msg.from_user.id, "Выберите действие:", reply_markup=keyboard.Keyboard_poll_edit)
        config.GR3 = True
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))

@dp.message_handler(commands=['poll_manager_gr4'])
async def managing_process4(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Последний отправленый опрос:")
        await bot.send_poll(chat_id=msg.from_user.id,
                            question=config.LAST_POLL_GR4.Poll.question,
                            options=config.LAST_POLL_GR4.Poll.options,
                            type=config.LAST_POLL_GR4.Poll.type,
                            correct_option_id=config.LAST_POLL_GR4.Poll.correct_option_id,
                            is_anonymous=config.LAST_POLL_GR4.Poll.is_anonymous,
                            allows_multiple_answers=config.LAST_POLL_GR4.Poll.allows_multiple_answers)
        await bot.send_message(msg.from_user.id, "Выберите действие:", reply_markup=keyboard.Keyboard_poll_edit)
        config.GR4 = True
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))


@dp.callback_query_handler(text="delete_poll")
async def deleting_message_process(call: types.CallbackQuery):
    if config.GR1:
        for i in range(len(config.LAST_POLL_GR1.chat_id)):
            chat_id_temp = config.LAST_POLL_GR1.chat_id[i]
            msg_id_temp = config.LAST_POLL_GR1.message_id[i]
            await bot.delete_message(chat_id_temp, msg_id_temp)
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, "Опрос удалён")
    if config.GR2:
        for i in range(len(config.LAST_POLL_GR2.chat_id)):
            chat_id_temp = config.LAST_POLL_GR2.chat_id[i]
            msg_id_temp = config.LAST_POLL_GR2.message_id[i]
            await bot.delete_message(chat_id_temp, msg_id_temp)
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, "Опрос удалён")
    if config.GR3:
        for i in range(len(config.LAST_POLL_GR3.chat_id)):
            chat_id_temp = config.LAST_POLL_GR3.chat_id[i]
            msg_id_temp = config.LAST_POLL_GR3.message_id[i]
            await bot.delete_message(chat_id_temp, msg_id_temp)
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, "Опрос удалён")
    if config.GR4:
        for i in range(len(config.LAST_POLL_GR4.chat_id)):
            chat_id_temp = config.LAST_POLL_GR4.chat_id[i]
            msg_id_temp = config.LAST_POLL_GR4.message_id[i]
            await bot.delete_message(chat_id_temp, msg_id_temp)
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.from_user.id, "Опрос удалён")



@dp.message_handler(commands=['message_manager_gr1'])
async def managing_process1(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Текст последнего сообщения:\n" + config.LAST_MSG_GR1.text,
                        reply_markup=keyboard.Keyboard_message_edit)
        config.GR1 = True
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))

@dp.message_handler(commands=['message_manager_gr2'])
async def managing_process2(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Текст последнего сообщения:\n" + config.LAST_MSG_GR2.text,
                        reply_markup=keyboard.Keyboard_message_edit)
        config.GR2 = True
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))

@dp.message_handler(commands=['message_manager_gr3'])
async def managing_process3(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Текст последнего сообщения:\n" + config.LAST_MSG_GR3.text,
                        reply_markup=keyboard.Keyboard_message_edit)
        config.GR3 = True
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))

@dp.message_handler(commands=['message_manager_gr4'])
async def managing_process4(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Текст последнего сообщения:\n" + config.LAST_MSG_GR4.text,
                        reply_markup=keyboard.Keyboard_message_edit)
        config.GR4 = True
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))


@dp.callback_query_handler(text="delete_message")
async def deleting_message_process(call: types.CallbackQuery):
    if config.GR1:
        for i in range(len(config.LAST_MSG_GR1.chat_id)):
            chat_id_temp = config.LAST_MSG_GR1.chat_id[i]
            msg_id_temp = config.LAST_MSG_GR1.message_id[i]
            await bot.delete_message(chat_id_temp, msg_id_temp)
            await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Сообщение удалено")
    if config.GR2:
        for i in range(len(config.LAST_MSG_GR2.chat_id)):
            chat_id_temp = config.LAST_MSG_GR2.chat_id[i]
            msg_id_temp = config.LAST_MSG_GR2.message_id[i]
            await bot.delete_message(chat_id_temp, msg_id_temp)
            await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Сообщение удалено")
    if config.GR3:
        for i in range(len(config.LAST_MSG_GR3.chat_id)):
            chat_id_temp = config.LAST_MSG_GR3.chat_id[i]
            msg_id_temp = config.LAST_MSG_GR3.message_id[i]
            await bot.delete_message(chat_id_temp, msg_id_temp)
            await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Сообщение удалено")
    if config.GR4:
        for i in range(len(config.LAST_MSG_GR4.chat_id)):
            chat_id_temp = config.LAST_MSG_GR4.chat_id[i]
            msg_id_temp = config.LAST_MSG_GR4.message_id[i]
            await bot.delete_message(chat_id_temp, msg_id_temp)
            await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Сообщение удалено")


@dp.callback_query_handler(text="edit_message")
async def editing_message_process(call: types.CallbackQuery):

    config.EDITING = True
    await bot.send_message(call.from_user.id, "Введите текст отредактированого сообщения:")
    await bot.answer_callback_query(call.id)


@dp.message_handler(commands=["solo_add_gr1"])
async def adding_solo_group1_process(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Введите id и название канала в формате (без пробела после запятой) :\n12345,Название канала")
        config.SOLO_ADD1 = True
        await process_getall()
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))


@dp.message_handler(commands=["solo_add_gr2"])
async def adding_solo_group1_process(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Введите id и название канала в формате (без пробела после запятой) :\n12345,Название канала")
        config.SOLO_ADD1 = True
        await process_getall()
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))


@dp.message_handler(commands=["solo_add_gr3"])
async def adding_solo_group1_process(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Введите id и название канала в формате (без пробела после запятой) :\n12345,Название канала")
        config.SOLO_ADD1 = True
        await process_getall()
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))


@dp.message_handler(commands=["solo_add_gr4"])
async def adding_solo_group1_process(msg: types.Message):
    await return_state()

    if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
        await msg.reply("Введите id и название канала в формате (без пробела после запятой) :\n12345,Название канала")
        config.SOLO_ADD1 = True
        await process_getall()
    else:
        await bot.send_message(msg.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                 "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                               + str(msg.from_user.id))


@dp.message_handler(commands=["del_group1"])
async def delete_process(message: types.Message):
    await return_state()

    if message.from_user.id == BOT_ADMIN1 or message.from_user.id == BOT_ADMIN2 or message.from_user.id == BOT_DEV:
        text = "Введите номер чата или канала: \n" + str(DB.getNames(group_1_path))
        await message.reply(text)
        config.DELETING1 = True
        await process_getall()

    else:
        await bot.send_message(message.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                     "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(message.from_user.full_name) + "\nUser ID:"
                               + str(message.from_user.id))


@dp.message_handler(commands=["del_group2"])
async def delete_process(message: types.Message):
    await return_state()

    if message.from_user.id == BOT_ADMIN1 or message.from_user.id == BOT_ADMIN2 or message.from_user.id == BOT_DEV:
        text = "Введите номер чата или канала: \n" + str(DB.getNames(group_2_path))
        await message.reply(text)
        config.DELETING2 = True

    else:
        await bot.send_message(message.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                     "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(message.from_user.full_name) + "\nUser ID:"
                               + str(message.from_user.id))


@dp.message_handler(commands=["del_group3"])
async def delete_process(message: types.Message):
    await return_state()

    if message.from_user.id == BOT_ADMIN1 or message.from_user.id == BOT_ADMIN2 or message.from_user.id == BOT_DEV:
        text = "Введите номер чата или канала: \n" + str(DB.getNames(group_3_path))
        await message.reply(text)
        config.DELETING3 = True
        await process_getall()

    else:
        await bot.send_message(message.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                     "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(message.from_user.full_name) + "\nUser ID:"
                               + str(message.from_user.id))


@dp.message_handler(commands=["del_group4"])
async def delete_process(message: types.Message):
    await return_state()

    if message.from_user.id == BOT_ADMIN1 or message.from_user.id == BOT_ADMIN2 or message.from_user.id == BOT_DEV:
        text = "Введите номер чата или канала: \n" + str(DB.getNames(group_4_path))
        await message.reply(text)
        config.DELETING4 = True
        await process_getall()

    else:
        await bot.send_message(message.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                     "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(message.from_user.full_name) + "\nUser ID:"
                               + str(message.from_user.id))


# - add Id`s and names to DB
@dp.message_handler(commands=["add_group1"])
async def addgroup1_handler(message: types.Message):
    await return_state()

    if message.from_user.id == BOT_ADMIN1 or message.from_user.id == BOT_ADMIN2 or message.from_user.id == BOT_DEV:
        id_of_chat = message.chat.id
        DB.add(ID=id_of_chat, name=message.chat.full_name, file_name=group_1_path)
        await process_getall()
        await bot.send_message(message.from_user.id, "Чат " + str(message.chat.full_name) + ' добавлен в группу "Заказчики"')
        await bot.delete_message(message.chat.id, message.message_id)

    else:
        await bot.send_message(message.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                     "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(message.from_user.full_name) + "\nUser ID:"
                               + str(message.from_user.id))


@dp.message_handler(commands=["add_group2"])
async def addgroup2_handler(message: types.Message):
    await return_state()

    if message.from_user.id == BOT_ADMIN1 or message.from_user.id == BOT_ADMIN2 or message.from_user.id == BOT_DEV:
        id_of_chat = message.chat.id
        DB.add(ID=id_of_chat, name=message.chat.full_name, file_name=group_2_path)
        await process_getall()
        await bot.send_message(message.from_user.id, "Чат " + str(message.chat.full_name) + " добавлен в группу 2")
        await bot.delete_message(message.chat.id, message.message_id)

    else:
        await bot.send_message(message.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                     "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(message.from_user.full_name) + "\nUser ID:"
                               + str(message.from_user.id))


@dp.message_handler(commands=["add_group3"])
async def addgroup3_handler(message: types.Message):
    await return_state()

    if message.from_user.id == BOT_ADMIN1 or message.from_user.id == BOT_ADMIN2 or message.from_user.id == BOT_DEV:
        id_of_chat = message.chat.id
        DB.add(ID=id_of_chat, name=message.chat.full_name, file_name=group_3_path)
        await process_getall()
        await bot.send_message(message.from_user.id, "Чат " + str(message.chat.full_name) + " добавлен в группу 3")
        await bot.delete_message(message.chat.id, message.message_id)

    else:
        await bot.send_message(message.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                     "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(message.from_user.full_name) + "\nUser ID:"
                               + str(message.from_user.id))


@dp.message_handler(commands=["add_group4"])
async def addgroup4_handler(message: types.Message):
    await return_state()

    if message.from_user.id == BOT_ADMIN1 or message.from_user.id == BOT_ADMIN2 or message.from_user.id == BOT_DEV:
        id_of_chat = message.chat.id
        DB.add(ID=id_of_chat, name=message.chat.full_name, file_name=group_4_path)
        await process_getall()
        await bot.send_message(message.from_user.id, "Чат " + str(message.chat.full_name) + " добавлен в группу 4")
        await bot.delete_message(message.chat.id, message.message_id)
    else:
        await bot.send_message(message.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                     "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(message.from_user.full_name) + "\nUser ID:"
                               + str(message.from_user.id))


# - add Id`s and names to DB --end--


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await return_state()

    if message.from_user.id == BOT_ADMIN1 or message.from_user.id == BOT_ADMIN2 or message.from_user.id == BOT_DEV:
        await message.answer("*Нажмите на кнопку ниже и создайте опрос или рассылку!*\n⚠️Осторожно!⚠️\n"
                             "Телеграм не разрешает отправлять НЕ анонимные опросы в телеграмм-канал.\n"
                             "При создании неанонимного опроса, аналатика будет недоступна)",
                             reply_markup=keyboard.Keyboard_Start, parse_mode="Markdown")
    else:
        await bot.send_message(message.from_user.id, "Вы не уполномочены отправлять команды в этот бот.\n"
                                                     "Обратитесь к Администратору.")
        await bot.send_message(RECOVER_ID, "Пользователь пытался отправить команду\n"
                               + "\nUsername of user: " + str(message.from_user.full_name) + "\nUser ID:"
                               + str(message.from_user.id))


@dp.callback_query_handler(text="gr1")
async def process_callback_gr1(call: types.CallbackQuery):
    print(config.MAILSHOT_FLAG)
    if config.MAILSHOT_FLAG:
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, 'Рассылка будет отправлена в группу "Заказчики". Введите текст: ')
        config.GR1 = True
    if config.POLL_FLAG:
        config.LAST_POLL_GR1.message_id.clear()
        config.LAST_POLL_GR1.chat_id.clear()
        config.LAST_POLL_GR1.poll_id.clear()
        config.OPTION_COUNTER1.clear()

        for id in DB.getIDs(group_1_path):
            last_poll = await bot.send_poll(chat_id=id,
                                question=config.POLL_BUF.question,
                                options=config.POLL_BUF.options,
                                type=config.POLL_BUF.type,
                                correct_option_id=config.POLL_BUF.correct_option_id,
                                is_anonymous=config.POLL_BUF.is_anonymous,
                                allows_multiple_answers=config.POLL_BUF.allows_multiple_answers)
            config.LAST_POLL_GR1.chat_id.append(last_poll.chat.id)
            config.LAST_POLL_GR1.message_id.append((last_poll.message_id))
            config.LAST_POLL_GR1.Poll = config.POLL_BUF
            config.LAST_POLL_GR1.poll_id.append(last_poll.poll.id)

        for i in range(len(config.LAST_POLL_GR1.Poll.options)):
            config.OPTION_COUNTER1.append(0)

        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, 'Опрос будет отправлен в группу "Заказчики"')


@dp.callback_query_handler(text='gr2')
async def process_callback_gr2(call: types.CallbackQuery):
    if config.MAILSHOT_FLAG:
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Рассылка будет отправлена в группу 2. Введите текст: ")
        config.GR2 = True
    if config.POLL_FLAG:
        config.LAST_POLL_GR2.message_id.clear()
        config.LAST_POLL_GR2.chat_id.clear()
        config.OPTION_COUNTER2.clear()

        for id in DB.getIDs(group_2_path):
            last_poll = await bot.send_poll(chat_id=id,
                                question=config.POLL_BUF.question,
                                options=config.POLL_BUF.options,
                                type=config.POLL_BUF.type,
                                correct_option_id=config.POLL_BUF.correct_option_id,
                                is_anonymous=config.POLL_BUF.is_anonymous,
                                allows_multiple_answers=config.POLL_BUF.allows_multiple_answers)
            config.LAST_POLL_GR2.chat_id.append(last_poll.chat.id)
            config.LAST_POLL_GR2.message_id.append((last_poll.message_id))
            config.LAST_POLL_GR2.Poll = config.POLL_BUF
            config.LAST_POLL_GR2.poll_id.append(last_poll.poll.id)

        for i in range(len(config.LAST_POLL_GR2.Poll.options)):
            config.OPTION_COUNTER2.append(0)


        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Опрос будет отправлен в группу 2")


@dp.callback_query_handler(text='gr3')
async def process_callback_gr3(call: types.CallbackQuery):
    if config.MAILSHOT_FLAG:
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Рассылка будет отправлена в группу 3. Введите текст: ")
        config.GR3 = True
    if config.POLL_FLAG:
        config.LAST_POLL_GR3.message_id.clear()
        config.LAST_POLL_GR3.chat_id.clear()
        config.OPTION_COUNTER3.clear()

        for id in DB.getIDs(group_3_path):
            last_poll = await bot.send_poll(chat_id=id,
                                question=config.POLL_BUF.question,
                                options=config.POLL_BUF.options,
                                type=config.POLL_BUF.type,
                                correct_option_id=config.POLL_BUF.correct_option_id,
                                is_anonymous=config.POLL_BUF.is_anonymous,
                                allows_multiple_answers=config.POLL_BUF.allows_multiple_answers)
            config.LAST_POLL_GR3.chat_id.append(last_poll.chat.id)
            config.LAST_POLL_GR3.message_id.append((last_poll.message_id))
            config.LAST_POLL_GR3.Poll = config.POLL_BUF
            config.LAST_POLL_GR3.poll_id.append(last_poll.poll.id)

        for i in range(len(config.LAST_POLL_GR3.Poll.options)):
            config.OPTION_COUNTER3.append(0)

        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Опрос будет отправлен в группу 3")


@dp.callback_query_handler(text='gr4')
async def process_callback_gr4(call: types.CallbackQuery):
    if config.MAILSHOT_FLAG:
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Рассылка будет отправлен в группу 4, введите текст:")
        config.GR4 = True
    if config.POLL_FLAG:
        config.LAST_POLL_GR4.message_id.clear()
        config.LAST_POLL_GR4.chat_id.clear()
        config.OPTION_COUNTER4.clear()

        for id in DB.getIDs(group_4_path):
            last_poll = await bot.send_poll(chat_id=id,
                                question=config.POLL_BUF.question,
                                options=config.POLL_BUF.options,
                                type=config.POLL_BUF.type,
                                correct_option_id=config.POLL_BUF.correct_option_id,
                                is_anonymous=config.POLL_BUF.is_anonymous,
                                allows_multiple_answers=config.POLL_BUF.allows_multiple_answers)
            config.LAST_POLL_GR4.chat_id.append(last_poll.chat.id)
            config.LAST_POLL_GR4.message_id.append((last_poll.message_id))
            config.LAST_POLL_GR4.Poll = config.POLL_BUF
            config.LAST_POLL_GR4.poll_id.append(last_poll.poll.id)

        for i in range(len(config.LAST_POLL_GR4.Poll.options)):
            config.OPTION_COUNTER4.append(0)

        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, "Опрос будет отправлен в группу 4")


@dp.message_handler(content_types=["poll"])
async def send_a_poll(message: types.message):
    await return_state()

    # save a poll
    config.POLL_BUF = Poll(
        poll_id=message.poll.id,
        question=message.poll.question,
        options=[o.text for o in message.poll.options],
        type=message.poll.type,
        correct_option_id=message.poll.correct_option_id,
        is_anonymous=message.poll.is_anonymous,
        allows_multiple_answers=message.poll.allows_multiple_answers
    )
    config.POLL_FLAG = True
    await bot.send_message(message.from_user.id, "Выберите группу для рассылки",
                           reply_markup=keyboard.Keyboard_Groups)


@dp.callback_query_handler(text = 'analitycs_poll')
async def analitycs_process(call: types.CallbackQuery):

    if config.GR1:
        counter = 1
        final_message = ""
        for option in config.OPTION_COUNTER1:
            final_message = final_message + "*Вариант " + str(counter) + ' - *' + str(option) + '\n'
            counter += 1
        await bot.send_message(call.from_user.id, final_message, parse_mode="Markdown")

    if config.GR2:
        counter = 1
        final_message = ""
        for option in config.OPTION_COUNTER2:
            final_message = final_message + "*Вариант " + str(counter) + ' - *' + str(option) + '\n'
            counter += 1
        await bot.send_message(call.from_user.id, final_message, parse_mode="Markdown")

    if config.GR3:
        counter = 1
        final_message = ""
        for option in config.OPTION_COUNTER3:
            final_message = final_message + "*Вариант " + str(counter) + ' - *' + str(option) + '\n'
            counter += 1
        await bot.send_message(call.from_user.id, final_message, parse_mode="Markdown")

    if config.GR4:
        counter = 1
        final_message = ""
        for option in config.OPTION_COUNTER4:
            final_message = final_message + "*Вариант " + str(counter) + ' - *' + str(option) + '\n'
            counter += 1
        await bot.send_message(call.from_user.id, final_message, parse_mode="Markdown")


@dp.poll_answer_handler()
async def handle_poll_answer(answer: types.PollAnswer):

    if answer.poll_id in config.LAST_POLL_GR1.poll_id:
        print("Gr1")
        for option in answer.option_ids:
            print(option)
            config.OPTION_COUNTER1[option] += 1

    if answer.poll_id in config.LAST_POLL_GR2.poll_id:
        print("Gr2")
        for option in answer.option_ids:
            print(option)
            config.OPTION_COUNTER2[option] += 1

    if answer.poll_id in config.LAST_POLL_GR3.poll_id:
        print("Gr3")
        for option in answer.option_ids:
            print(option)
            config.OPTION_COUNTER3[option] += 1

    if answer.poll_id in config.LAST_POLL_GR4.poll_id:
        print("Gr4")
        for option in answer.option_ids:
            print(option)
            config.OPTION_COUNTER4[option] += 1



@dp.message_handler()
async def process_mailshot(msg: types.Message):
    # Отправка рассылки
    if msg.text == "Сделать рассылку":
        if msg.from_user.id == BOT_ADMIN1 or msg.from_user.id == BOT_ADMIN2 or msg.from_user.id == BOT_DEV:
            config.MAILSHOT_FLAG = True
            await process_callback_button1(msg)
        else:
            await bot.send_message(msg.from_user.id, "Вы не уполномочены писать в этот бот.\n"
                                                     "Обратитесь к Администратору.")
            await bot.send_message(RECOVER_ID, "Пользователь пытался отправить рассылку\n"
                                   + "\nUsername of user: " + str(msg.from_user.full_name) + "\nUser ID:"
                                   + str(msg.from_user.id))
    ###
    # Adding an id and name by yourself
    if config.SOLO_ADD1:
        message_text = msg.text
        id = message_text.split(',')[0]
        name = message_text.split(',')[1]
        DB.add(id, name, group_1_path)
        config.SOLO_ADD1 = False
    if config.SOLO_ADD2:
        message_text = msg.text
        id = message_text.split(',')[0]
        name = message_text.split(',')[1]
        DB.add(id, name, group_2_path)
        config.SOLO_ADD2 = False
    if config.SOLO_ADD3:
        message_text = msg.text
        id = message_text.split(',')[0]
        name = message_text.split(',')[1]
        DB.add(id, name, group_3_path)
        config.SOLO_ADD3 = False
    if config.SOLO_ADD4:
        message_text = msg.text
        id = message_text.split(',')[0]
        name = message_text.split(',')[1]
        DB.add(id, name, group_4_path)
        config.SOLO_ADD4 = False

    #sending a mailshot
    if config.MAILSHOT_FLAG:
        if config.GR1:
            config.LAST_MSG_GR1.text = msg.text
            config.LAST_MSG_GR1.message_id.clear()
            config.LAST_MSG_GR1.chat_id.clear()
            for id in DB.getIDs(group_1_path):
                #saving a data for deleting last message
                message_temp = await bot.send_message(int(id), str(msg.text))
                config.LAST_MSG_GR1.message_id.append(message_temp.message_id)
                config.LAST_MSG_GR1.chat_id.append(message_temp.chat.id)
            await msg.reply("Рассылка отправлена!")
            config.GR1 = False
            config.MAILSHOT_FLAG = False
        if config.GR2:
            config.LAST_MSG_GR2.text = msg.text
            config.LAST_MSG_GR2.message_id.clear()
            config.LAST_MSG_GR2.chat_id.clear()
            for id in DB.getIDs(group_2_path):
                #saving a data for deleting last message
                message_temp = await bot.send_message(int(id), str(msg.text))
                config.LAST_MSG_GR2.message_id.append(message_temp.message_id)
                config.LAST_MSG_GR2.chat_id.append(message_temp.chat.id)
            await msg.reply("Рассылка отправлена!")
            config.GR2 = False
            config.MAILSHOT_FLAG = False
        if config.GR3:
            config.LAST_MSG_GR3.text = msg.text
            config.LAST_MSG_GR3.message_id.clear()
            config.LAST_MSG_GR3.chat_id.clear()
            for id in DB.getIDs(group_3_path):
                #saving a data for deleting last message
                message_temp = await bot.send_message(int(id), str(msg.text))
                config.LAST_MSG_GR3.message_id.append(message_temp.message_id)
                config.LAST_MSG_GR3.chat_id.append(message_temp.chat.id)
            await msg.reply("Рассылка отправлена!")
            config.GR3 = False
            config.MAILSHOT_FLAG = False
        if config.GR4:
            config.LAST_MSG_GR4.text = msg.text
            config.LAST_MSG_GR4.message_id.clear()
            config.LAST_MSG_GR4.chat_id.clear()
            for id in DB.getIDs(group_4_path):
                #saving a data for deleting last message
                message_temp = await bot.send_message(int(id), str(msg.text))
                config.LAST_MSG_GR4.message_id.append(message_temp.message_id)
                config.LAST_MSG_GR4.chat_id.append(message_temp.chat.id)
            await msg.reply("Рассылка отправлена!")
            config.GR4 = False
            config.MAILSHOT_FLAG = False
    if config.DELETING1:
        DB.delete(int(msg.text), group_1_path)
        print('DELETING1 flag detected')
        config.DELETING1 = False
        await bot.send_message(msg.from_user.id, 'Чат удален из группы "Заказчики"')
    if config.DELETING2:
        DB.delete(int(msg.text), group_2_path)
        print('DELETING2 flag detected')
        config.DELETING2 = False
        await bot.send_message(msg.from_user.id, "Чат удален из группы 2")
    if config.DELETING3:
        DB.delete(int(msg.text), group_3_path)
        print('DELETING3 flag detected')
        config.DELETING3 = False
        await bot.send_message(msg.from_user.id, "Чат удален из группы 3")
    if config.DELETING4:
        DB.delete(int(msg.text), group_4_path)
        print('DELETING4 flag detected')
        config.DELETING4 = False
        await bot.send_message(msg.from_user.id, "Чат удален из группы 4")

    if config.EDITING:
        if config.GR1:
            LAST_MSG_BUF = config.Mesage_recover([], [], msg.text)
            for i in range(len(config.LAST_MSG_GR1.chat_id)):
                chat_id_temp = config.LAST_MSG_GR1.chat_id[i]
                msg_id_temp = config.LAST_MSG_GR1.message_id[i]
                code = await bot.edit_message_text(msg.text, chat_id_temp, msg_id_temp)
                LAST_MSG_BUF.chat_id.append(code.chat.id)
                LAST_MSG_BUF.message_id.append(code.message_id)
            config.LAST_MSG_GR1 = LAST_MSG_BUF
            await msg.reply("Сообщение отредактирвано")
        if config.GR2:
            LAST_MSG_BUF = config.Mesage_recover([], [], msg.text)
            for i in range(len(config.LAST_MSG_GR2.chat_id)):
                chat_id_temp = config.LAST_MSG_GR2.chat_id[i]
                msg_id_temp = config.LAST_MSG_GR2.message_id[i]
                code = await bot.edit_message_text(msg.text, chat_id_temp, msg_id_temp)
                LAST_MSG_BUF.chat_id.append(code.chat.id)
                LAST_MSG_BUF.message_id.append(code.message_id)
            config.LAST_MSG_GR2 = LAST_MSG_BUF
            await msg.reply("Сообщение отредактирвано")
        if config.GR3:
            LAST_MSG_BUF = config.Mesage_recover([], [], msg.text)
            for i in range(len(config.LAST_MSG_GR3.chat_id)):
                chat_id_temp = config.LAST_MSG_GR3.chat_id[i]
                msg_id_temp = config.LAST_MSG_GR3.message_id[i]
                code = await bot.edit_message_text(msg.text, chat_id_temp, msg_id_temp)
                LAST_MSG_BUF.chat_id.append(code.chat.id)
                LAST_MSG_BUF.message_id.append(code.message_id)
            config.LAST_MSG_GR3 = LAST_MSG_BUF
            await msg.reply("Сообщение отредактирвано")
        if config.GR4:
            LAST_MSG_BUF = config.Mesage_recover([], [], msg.text)
            for i in range(len(config.LAST_MSG_GR4.chat_id)):
                chat_id_temp = config.LAST_MSG_GR4.chat_id[i]
                msg_id_temp = config.LAST_MSG_GR4.message_id[i]
                code = await bot.edit_message_text(msg.text, chat_id_temp, msg_id_temp)
                LAST_MSG_BUF.chat_id.append(code.chat.id)
                LAST_MSG_BUF.message_id.append(code.message_id)

            config.LAST_MSG_GR4 = LAST_MSG_BUF
            await msg.reply("Сообщение отредактирвано")# не удалаяет
# ---------main code--------


if __name__ == '__main__':
    executor.start_polling(dp)
