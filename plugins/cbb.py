#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "menu":
        await query.message.edit_text(
            text = f"<b>ᴍᴇɴᴜ ꜰᴇᴀᴛᴜʀᴇᴅ</b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📲ꜰᴏʟʟᴏᴡ ᴜꜱ ", callback_data="media")
                 ],
              [InlineKeyboardButton("🔐 ᴘʀᴇᴍɪᴜᴍ ᴠɪᴘ ", callback_data="premium"),
              InlineKeyboardButton("💰 ꜱᴛᴏʀᴇ ", callback_data="promotion",)],
                    [InlineKeyboardButton('🌐 ᴡᴇʙꜱɪᴛᴇ ', url='https://px-z.blogspot.com')],
                   [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
                ]
            )
        )

    elif data == "media":
        await query.message.edit_text(
            text=f"<blockquote>👋 hello user : {query.from_user.username}\n\nꜰᴏʟʟᴏᴡ ꜱᴏᴄɪᴀʟ ᴍᴇᴅɪᴀ ᴏꜰꜰɪᴄɪᴀʟ</blockquote>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton('📱 ɪɴꜱᴛᴀɢʀᴀᴍ', url='https://Instagram.com/pxz_official'),
                InlineKeyboardButton('📲 ᴡʜᴀᴛꜱᴀᴘᴘ', url='https://whatsapp.com/channel/0029Vaj27FHLo4hWYvLaUM00')
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )

    if data == "developer":
        await query.message.edit_text(
            text = f"<blockquote><b> ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ʜʀʙᴛᴇᴀᴍ</a>\nꜱᴜᴘᴘᴏʀᴛ : <a href='https://t.me/HRBsupport'>ʜʀʙᴛᴇᴀᴍ ꜱᴜᴘᴘᴏʀᴛ</a>\nꜱᴜᴘᴘᴏʀᴛ ᴜᴘᴅᴀᴛᴇ : <a href='https://t.me/HRBsupport_official'>ʜʀʙᴛᴇᴀᴍ ꜱᴜᴘᴘᴏʀᴛ ᴜᴘᴅᴀᴛᴇ</a>\nꜱᴛᴏʀᴇ : <a href='https://t.me/HRBstore_official'>ʜʀʙꜱᴛᴏʀᴇ </a></b></blockquote>",
           disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ 1', url='https://t.me/dammingyu'),
                    InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ 2', url='https://t.me/Honorsteam')],
                   [ InlineKeyboardButton('🛂 ꜱᴜᴘᴘᴏʀᴛ ', url='https://t.me/HRBsupport')],
                   [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
                ]
            )
        )

    elif data == "donate":
        await query.message.edit_text(
            text = f"<b>ᴅᴏɴᴀᴛᴇ - ʜʀʙꜰᴀᴍɪʟʏ</b>\nᴊɪᴋᴀ ᴋᴀʟɪᴀɴ ꜱᴜᴋᴀ ꜱᴀᴍᴀ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴋᴀᴍɪ ʙᴀɢɪᴋᴀɴ ꜱᴇᴄᴀʀᴀ ɢʀᴀᴛɪꜱ/ʙᴀʏᴀʀᴀɴ, ɪɴɢɪɴ ʙᴇʀʙᴀɢɪ (ᴅᴏɴᴀꜱɪ) ᴋᴇᴘᴀᴅᴀ ᴘxᴢᴛᴇᴀᴍ? ꜱɪʟᴀʜᴋᴀɴ ᴘɪʟɪʜ ᴠɪᴀ ᴅᴏɴᴀꜱɪ\n ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴛʜᴇ ᴠɪᴅᴇᴏꜱ ᴡᴇ ꜱʜᴀʀᴇ ꜰᴏʀ ꜰʀᴇᴇ/ᴘᴀɪᴅ, ᴡᴀɴᴛ ᴛᴏ ꜱʜᴀʀᴇ (ᴅᴏɴᴀᴛᴇ) ᴛᴏ ᴘxᴢᴛᴇᴀᴍ? ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴠɪᴀ ᴅᴏɴᴀᴛɪᴏɴ",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
              [  InlineKeyboardButton('🧾 ꜱᴀᴡᴇʀɪᴀ', url='https://saweria.co/PXZsupport'),
                InlineKeyboardButton('🧾 ᴘᴀʏᴘᴀʟ', url='https://paypal.me/PEXLAND')
          ],
                [InlineKeyboardButton('🧾 ᴛʀᴀᴋᴛᴇᴇʀ', url='https://trakteer.id/hrbofficial/tip')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
            ])            
        )
    
    elif data == "premium":
        await query.message.edit_text(
            text = f"<b>ʟɪꜱᴛ ᴛᴏ ʙᴇ ᴘʀᴇᴍɪᴜᴍ ᴏꜰ ᴘxᴢᴠɪᴘ\n<blockquote>100 ᴠɪᴅᴇᴏ 5ᴋ\n200 ᴠɪᴅᴇᴏ 10ᴋ\n300 ᴠɪᴅᴇᴏ 15ᴋ\n400 ᴠɪᴅᴇᴏ 20ᴋ\n500 ᴠɪᴅᴇᴏ 25ᴋ\n600 ᴠɪᴅᴇᴏ 30ᴋ\n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʙᴜʏ ᴠɪᴘ, ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ</blockquote></b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🔓 ꜱᴀᴡᴇʀɪᴀ', url='https://saweria.co/PXZsupport'),
                InlineKeyboardButton('🔓 ᴘᴀʏᴘᴀʟ', url='https://paypal.me/PEXLAND')],
                [InlineKeyboardButton('🔓 ᴛʀᴀᴋᴛᴇᴇʀ', url='https://trakteer.id/hrbofficial/tip')],
                [InlineKeyboardButton('🛂 ᴄᴏɴᴛᴀᴄᴛ', url='https://t.me/pxzstore_team')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
        )
    elif data == "promotion":
        await query.message.edit_text(
            text = f"<b>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴘʀᴏᴍᴏᴛɪᴏɴ ᴠɪᴅᴇᴏ/ᴘʜᴏᴛᴏ/ᴇᴛᴄ ᴄᴏɴᴛᴀᴄᴛ ꜱᴛᴏʀᴇ ᴛᴇᴀᴍ👇</b>",  disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🤖 ᴄᴏɴᴛᴀᴄᴛ', url='https://t.me/HonorsTeam'),
                InlineKeyboardButton('📤 ᴜᴘʟᴏᴀᴅᴇᴅ', url='https://t.me/+U3RYX-jKJTxjYzk1')],
                [
                InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
    )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
