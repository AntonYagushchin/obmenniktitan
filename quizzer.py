from typing import List


class Poll:
    def __init__(self, poll_id, question, options, type, correct_option_id, is_anonymous, allows_multiple_answers):
        # Используем подсказки типов, чтобы было проще ориентироваться.
        self.quiz_id: str = poll_id  # ID опроса. Изменится после отправки от имени бота
        self.question: str = question  # Текст вопроса
        self.options: List[str] = [*options]  # "Распакованное" содержимое массива m_options в массив options
        self.type: str = type
        self.correct_option_id: int = correct_option_id  # ID правильного ответа
        self.is_anonymous: bool = is_anonymous
        self.allows_multiple_answers: bool = allows_multiple_answers

        self.chat_id: int = 0  # Чат, в котором опубликована викторина
        self.message_id: int = 0  # Сообщение с викториной (для закрытия)

