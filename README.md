# Telebot Memory (telebot_mem)
Telebot with memory extension. It supports add a database backend to save chat histories.

## Quick start
```python
@bot.message_handler(func=lambda message: True)
@memdb.memorize
def echo_message(message):
    ...
```
Refer to [echo bot example with mongodb](examples/echo_bot_mongo_example.py)

## Roadmap
### Beta (v0.x) API will subject to change
- [] Test interface for mongodb support
