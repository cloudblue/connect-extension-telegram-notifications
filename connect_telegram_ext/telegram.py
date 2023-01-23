from html.parser import HTMLParser

import telegram


class TelegramHTMLParser(HTMLParser):
    """
    A class that inherits from HTMLParser and overrides
    the handle_data, handle_starttag, handle_endtag methods
    to escape all HTML tags except the ones specified in the exceptions list.
    """
    def __init__(self, exceptions=None):
        super().__init__()
        if exceptions is None:
            exceptions = ["b", "i", "a", "code", "pre"]
        self.exceptions = exceptions
        self.result = ""
        self.tags_stack = []

    def handle_data(self, data):
        self.result += data

    def handle_starttag(self, tag, attrs):
        self.tags_stack.append(tag)
        if tag in self.exceptions:
            self.result += "<" + tag + ">"
        else:
            self.result += "&lt;" + tag + "&gt;"

    def handle_endtag(self, tag):
        if self.tags_stack:
            if tag == self.tags_stack[-1]:
                self.tags_stack.pop()
                if tag in self.exceptions:
                    self.result += "</" + tag + ">"
                    return
        self.result += "&lt;/" + tag + "&gt;"


def convert_unsupported_tags(message_with_tags, allowed_tags=None):
    """
    Escapes all HTML tags in a string except for the ones specified in the exceptions list.

    :param message_with_tags: The input string containing HTML tags
    :type message_with_tags: str
    :param allowed_tags: List of HTML tags that should not be escaped
    :type allowed_tags: List[str]
    :return: The input string with all HTML tags escaped, except for the exceptions
    :rtype: str
    """
    parser = TelegramHTMLParser(allowed_tags)
    parser.feed(message_with_tags)
    return parser.result


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
