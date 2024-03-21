from telebot_mem.db import MemDB

from pymongo import MongoClient
from telebot.types import Message

class MongoDB(MemDB):
    def __init__(self, *args, **kwargs):
        self.client = MongoClient(*args, **kwargs)

    def insert_message(self, message: Message):
        
        self.client.messages.insert_one(message)

    def get_message(self, message_id):
        return self.client.messages.find_one({"_id": message_id})

    def validate(self):
        # check message collection exists
        return "messages" in self.client.list_collection_names()

    # decorator methods
    def memorize(self, func):
        def wrapper(*args, **kwargs):
            self.insert_message(func(*args, **kwargs))

        return wrapper
