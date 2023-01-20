import re

import telegram


def convert_unsupported_tags(message_with_tags):
    return re.sub(
        r'<(?!(\/?(b|i|a href|code|pre)\b))[^>]+>',
        lambda m: m.group().replace("<", "&lt;").replace(">", "&gt;"),
        message_with_tags,
    )


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
        return bot.send_message(
            self.chat_id,
            convert_unsupported_tags(message),
            parse_mode=telegram.constants.PARSEMODE_HTML,
        )
