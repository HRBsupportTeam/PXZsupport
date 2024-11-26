@Bot.on_message(filters.command('ch2l') & filters.private)
async def gen_link_encoded(client: Bot, message: Message):
    try:
        hash = await client.ask(text="Enter the code here... \n /cancel to cancel the operation",chat_id = message.from_user.id, timeout=60)
    except Exception as e:
        print(e)
        await hash.reply(f"ꜱᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ⚠️{e}")
        return
    if hash.text == "/cancel":
        await hash.reply("ᴄᴀɴᴄᴇʟʟᴇᴅ!")
        return
    link = f"https://t.me/{client.username}?start={hash.text}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("➡️ ᴄʟɪᴄᴋ ʜᴇʀᴇ ", url=link)]])
    await hash.reply_text(f"<b>🧑‍💻 ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ɢᴇɴᴇʀᴀᴛᴇᴅ ʟɪɴᴋ", quote=True, reply_markup=reply_markup)
    return
