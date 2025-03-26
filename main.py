from bot import *
from handlers.commands import *

print("Start polling")
bot.infinity_polling(30, long_polling_timeout=30)