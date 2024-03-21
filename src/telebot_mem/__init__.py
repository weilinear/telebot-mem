
# Monkey patching telebot to save json messages
from telebot import types

# Override the de_json method for messages to also save a copy of input strings
types.Message._de_json = types.Message.de_json
types.Message.de_json = lambda self, json_string: self._de_json(json_string) and self.__setattr__("json", json_string)

