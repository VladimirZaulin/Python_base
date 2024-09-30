#!/usr/pycharmprojects/bot_env
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll,VkBotEventType
from random import randint
import logging
try:
    import settings
except ImportError:
    exit('DO cp settings.py.default settings.py and set token')


group_id = 193037169

log = logging.getLogger('bot')

def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter((logging.Formatter("%(levelname)s %(message)s")))
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler("bot.log")
    file_handler.setFormatter((logging.Formatter(
                        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M')))
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)
    stream_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

class Bot:
    """
    Echo bot for vk.com
    Use python 3.12
    """
    def __init__(self, group_id, token):
        """
        :param group_id: id from vk group
        :param token: secret token
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """ Запуск бота """
        for event in  self.long_poller.listen():
           try:
               self.on_event(event)
           except Exception:
               log.exception("Ошибка в обработке события")

    def on_event(self, event):
        """
        Отправляет сообщение назад, если это текст.
        :param event: VkBotMessageEvent
        :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug(f"отправляем ему: {event.object.message['text']}")
            self.api.messages.send(message=f'Это ты -- {event.object.message["text"]}🙂!',
                                   random_id = randint(0,2 **20),
                                   peer_id = event.object.message['peer_id'])
        else:
            log.info("Мы пока не умеет обрабатывать %s",event.type)


if __name__ == "__main__":
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()