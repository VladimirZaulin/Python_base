from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from vk_api.bot_longpoll import VkBotMessageEvent

from bot import Bot

class Test1(TestCase):
    # self.RAW_EVENT = RAW_EVENT
    RAW_EVENT = {'group_id': 193037169, 'type': 'message_new',
                 'event_id': '0d142ce614aac4858e3d8bba55c58069e4cbb486', 'v': '5.199',
                 'object': {'message': {'date': 1727726444, 'from_id': 18012496, 'id': 103, 'version': 10000244,
                  'out': 0, 'important': False, 'is_hidden': False, 'attachments': [], 'conversation_message_id': 103,
                'fwd_messages': [], 'text': 'Дризлинг', 'peer_id': 18012496, 'random_id': 0},
                            'client_info': {'button_actions': ['text', 'vkpay', 'open_app', 'location',
                'open_link', 'callback', 'intent_subscribe', 'intent_unsubscribe'], 'keyboard': True,
                                            'inline_keyboard': True, 'carousel': True, 'lang_id': 0}}
    }
    def test_ok(self):
        count = 5
        obj = {'a':1}
        events = [obj] * count # {},{},{}
        long_poller_mock = Mock(return_value = events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock
        with patch('bot.vk_api.VkApi'):
            with patch ('bot.VkBotLongPoll', return_value = long_poller_listen_mock):
                bot = Bot('','')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)
        send_mock = Mock()
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('','')
                bot.api = Mock()
                bot.api.messages.send = send_mock

                bot.on_event(event)

        send_mock.assert_called_once_with(
            message=f'Это ты -- {self.RAW_EVENT["object"]['message']["text"]}🙂!',
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['message']['peer_id']
        )
