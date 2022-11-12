from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response

chatbot = ChatBot(
    'Magic Eightball',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    response_selection_method=get_random_response
)
