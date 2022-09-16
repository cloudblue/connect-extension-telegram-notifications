import telegram


class TelegramClient:
    def __init__(
        self,
        token,
        chat_id,
    ):
        self.token = token
        self.chat_id = chat_id

    def send_message(self, message):
        bot = telegram.Bot(self.token)
        bot.send_message(self.chat_id, message)
