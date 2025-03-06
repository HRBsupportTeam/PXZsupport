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
                InlineKeyboardButton('📲 ᴡʜᴀᴛꜱᴀᴘᴘ', url='https://whatsapp.com/channel/0029VayADxyISTkIw9MPGs0i')
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )

    elif data == "update":
        await query.message.edit_text(
            text=f"<blockquote>👋 hello user : {query.from_user.username}\n\nUntuk update selanjutnya bisa join channel Support team\n\n For further updates, you can join the Support team channel\n\n 如需进一步更新，您可以加入支持团队频道</blockquote>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton('🗞️ ᴄʟɪᴄᴋ ʜᴇʀᴇ', url='https://t.me/HRBsupport_official')],
                
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
                    [InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ¹', url='https://t.me/dammingyu'),
                    InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ²', url='https://t.me/Honorsteam')],
                   [ InlineKeyboardButton('🛂 ꜱᴜᴘᴘᴏʀᴛ¹ ', url='https://t.me/HRBsupport'),
                    InlineKeyboardButton('🛂 ꜱᴜᴘᴘᴏʀᴛ² ', url='https://t.me/HonorsSupport')],
                   [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
                  ])
        )

    elif data == "donate":
        await query.message.edit_text(
            text = f"<b>ᴅᴏɴᴀᴛᴇ - ʜʀʙꜰᴀᴍɪʟʏ</b>\nᴊɪᴋᴀ ᴋᴀʟɪᴀɴ ꜱᴜᴋᴀ ꜱᴀᴍᴀ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴋᴀᴍɪ ʙᴀɢɪᴋᴀɴ ꜱᴇᴄᴀʀᴀ ɢʀᴀᴛɪꜱ/ʙᴀʏᴀʀᴀɴ, ɪɴɢɪɴ ʙᴇʀʙᴀɢɪ (ᴅᴏɴᴀꜱɪ) ᴋᴇᴘᴀᴅᴀ ᴘxᴢᴛᴇᴀᴍ? ꜱɪʟᴀʜᴋᴀɴ ᴘɪʟɪʜ ᴠɪᴀ ᴅᴏɴᴀꜱɪ\n ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴛʜᴇ ᴠɪᴅᴇᴏꜱ ᴡᴇ ꜱʜᴀʀᴇ ꜰᴏʀ ꜰʀᴇᴇ/ᴘᴀɪᴅ, ᴡᴀɴᴛ ᴛᴏ ꜱʜᴀʀᴇ (ᴅᴏɴᴀᴛᴇ) ᴛᴏ ᴘxᴢᴛᴇᴀᴍ? ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴠɪᴀ ᴅᴏɴᴀᴛɪᴏɴ",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
              [  InlineKeyboardButton('🧾 ꜱᴀᴡᴇʀɪᴀ', url='https://saweria.co/PXZsupport'),
                InlineKeyboardButton('🧾 ᴘᴀʏᴘᴀʟ', url='https://paypal.me/PEXLAND')
          ],
                [  InlineKeyboardButton('🧾 ᴅᴀɴᴀ', url='https://i.postimg.cc/9M0XjWKX/qr-ID1024361924490-24-02-25-174033686-1740336867013.jpg'),
                InlineKeyboardButton('🧾 ᴛʀᴀᴋᴛᴇᴇʀ', url='https://trakteer.id/hrbofficial/tip')
          ],
                [  InlineKeyboardButton('🧾 ᴀʟɪᴘᴀʏ ᴄᴏᴍɪɴɢ ꜱᴏᴏɴ', url='https://t.me/HonorsSupport')],
                
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
            ])            
        )

                elif data == "media":
        await query.message.edit_text(
            text=f"<blockquote>👋 hello user : {query.from_user.username}\n\nꜰᴏʟʟᴏᴡ ꜱᴏᴄɪᴀʟ ᴍᴇᴅɪᴀ ᴏꜰꜰɪᴄɪᴀʟ</blockquote>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton('📱 ɪɴꜱᴛᴀɢʀᴀᴍ', url='https://Instagram.com/pxz_official'),
                InlineKeyboardButton('📲 ᴡʜᴀᴛꜱᴀᴘᴘ', url='https://whatsapp.com/channel/0029VayADxyISTkIw9MPGs0i')
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
    )
    
    elif data == "languages":
        await query.message.edit_text(
            text = f"<b>ᴄᴏᴍɪɴɢ ꜱᴏᴏɴ\nɪɴᴅᴏɴᴇꜱɪᴀɴ\nᴇɴɢʟɪꜱʜ\nᴄʜɪɴᴀ\nᴊᴀᴘᴀɴ\nᴋᴏʀᴇᴀ</b>",disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🇮🇩ɪɴᴅᴏɴᴇꜱɪᴀ', callback_data = 'menu'),
                InlineKeyboardButton('🔓 ᴘᴀʏᴘᴀʟ', url='menuen')],
                [InlineKeyboardButton('🔓 ᴅᴀɴᴀ', url='menujp'),
                InlineKeyboardButton('🔓 ᴅᴀɴᴀ', url='menuch')],
                [InlineKeyboardButton('🛂 ᴄᴏɴᴛᴀᴄᴛ', url='menukr')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
        )
    elif data == "promotion":
        await query.message.edit_text(
            text = f"<b>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴘʀᴏᴍᴏᴛɪᴏɴ ᴠɪᴅᴇᴏ/ᴘʜᴏᴛᴏ/ᴇᴛᴄ ᴄᴏɴᴛᴀᴄᴛ ꜱᴛᴏʀᴇ ᴛᴇᴀᴍ👇</b>",  disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🤖 ᴄᴏɴᴛᴀᴄᴛ', url='https://t.me/HonorsTeamBot'),
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
