from quizzer import Poll
from typing import List

class Poll_recover:
    def __init__(self, poll_id, chat_id, message_id, Poll):
        self.poll_id:List[int] = poll_id
        self.chat_id: List[int] = [*chat_id]
        self.message_id: List[int] = [*message_id]
        self.Poll = Poll


class Mesage_recover:
    def __init__(self, chat_id, message_id, text):
        self.chat_id: List[int] = [*chat_id]
        self.message_id: List[int] = [*message_id]
        self.text: str = text

TOKEN = "5073729215:AAHJXRSg-AmD7dD8RCiPyb3NSAfu7ZqjvGU"

BOT_DEV = 573711538
BOT_ADMIN1 = 1297108936
BOT_ADMIN2 = -1

RECOVER_ID = -1001493165992


MAILSHOT_FLAG = False
POLL_FLAG = False

SOLO_ADD1 = False
SOLO_ADD2 = False
SOLO_ADD3 = False
SOLO_ADD4 = False

GR1 = False
GR2 = False
GR3 = False
GR4 = False

DELETING1 = False
DELETING2 = False
DELETING3 = False
DELETING4 = False

CATCH_MSG_GR1 = False
CATCH_MSG_GR2 = False
CATCH_MSG_GR3 = False
CATCH_MSG_GR4 = False

EDITING = False

POLL_BUF = Poll(-1, "Еще не было опроса", ["Вариант1", "Вариант2"], "regular", 1, True, True)

LAST_POLL_GR1 = Poll_recover([-1], [-1], [-1], Poll(-1, "Еще не было опроса", ["Вариант1", "Вариант2"], "regular", 1, True, True))
LAST_POLL_GR2 = Poll_recover([-1], [-1], [-1], Poll(-1, "Еще не было опроса", ["Вариант1", "Вариант2"], "regular", 1, True, True))
LAST_POLL_GR3 = Poll_recover([-1], [-1], [-1], Poll(-1, "Еще не было опроса", ["Вариант1", "Вариант2"], "regular", 1, True, True))
LAST_POLL_GR4 = Poll_recover([-1], [-1], [-1], Poll(-1, "Еще не было опроса", ["Вариант1", "Вариант2"], "regular", 1, True, True))

OPTION_COUNTER1 = []
OPTION_COUNTER2 = []
OPTION_COUNTER3 = []
OPTION_COUNTER4 = []



LAST_MSG_GR1 = Mesage_recover([-1], [-1], "Еще не было сообщений в эту группу")
LAST_MSG_GR2 = Mesage_recover([-1], [-1], "Еще не было сообщений в эту группу")
LAST_MSG_GR3 = Mesage_recover([-1], [-1], "Еще не было сообщений в эту группу")
LAST_MSG_GR4 = Mesage_recover([-1], [-1], "Еще не было сообщений в эту группу")



EDIT_MSG_TEXT = ''