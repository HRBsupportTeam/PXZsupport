from pyrogram import filters, enums
from pyrogram.types import Message
from bot import Bot




@Bot.on_message(filters.command("vip") & filters.private)
async def user_vip(client, message):
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        user_vip = message.chat.vip
        await message.reply_text(
            f"<b>Your're is :</b> <code>{user_vip}</code>", 
            quote=True
        )
        





# HRBdeveloper 
# Don't Remove Credit 🥺
# Telegram Channel @HRBprojct
# Backup Channel @HRBsupport_bot
# Developer @HRBdeveloper
