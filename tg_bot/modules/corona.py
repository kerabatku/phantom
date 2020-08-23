import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "Apakah benar corona hanya konspirasi?",
    "🧼Rajin cuci tangan",
    "🚴‍♂️Olahraga dan tidur yang cukup🛌 Untuk meningkatkan imunitas tubuh",
    "🛀Rajin mandi dengan air bersih",
    "👬Jaga jarak",
    "😷Sedia dan pakai masker jika bepergian",
    "Hindari kebiasaan memegang mulut dan hidung tanpa cuci tangan terlebih dahulu",
    "Makan makanan yang sehat dan higienis",
    "#Dirumahaja kalo gaada yang penting dilakukan diluar",
  )

@run_async
def corona(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /corona  😷.
"""

__mod_name__ = "StaySafe"

CRNA_HANDLER = DisableAbleCommandHandler("corona", corona)

dispatcher.add_handler(CRNA_HANDLER)
