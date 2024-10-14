#(©)AnimeXyz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, CHANNEL_ID, PORT

name ="""
 BY HRBsupport
"""


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("ʙᴏᴛ ᴄᴀɴ'ᴛ ᴇxᴘᴏʀᴛ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ꜰʀᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ!")
                self.LOGGER(__name__).warning(f"ᴘʟᴇᴀꜱᴇ ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ FORCE_SUB_CHANNEL ᴠᴀʟᴜᴇ ᴀɴᴅ ᴍᴀᴋᴇ ꜱᴜʀᴇ ʙᴏᴛ ɪꜱ ᴀᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜꜱᴇʀꜱ ᴠɪᴀ ʟɪɴᴋ ᴘᴇʀᴍɪꜱꜱɪᴏɴ, ᴄᴜʀʀᴇɴᴛ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ ᴠᴀʟᴜᴇ: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nʙᴏᴛ ꜱᴛᴏᴘᴘᴇᴅ. ᴊᴏɪɴ https://t.me/HRBsupport ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛ")
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("ʙᴏᴛ ᴄᴀɴ'ᴛ ᴇxᴘᴏʀᴛ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ꜰʀᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ 2 ᴄʜᴀɴɴᴇʟ!")
                self.LOGGER(__name__).warning(f"ᴘʟᴇᴀꜱᴇ ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ FORCE_SUB_CHANNEL2 ᴠᴀʟᴜᴇ ᴀɴᴅ ᴍᴀᴋᴇ ꜱᴜʀᴇ ʙᴏᴛ ɪꜱ ᴀᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜꜱᴇʀꜱ ᴠɪᴀ ʟɪɴᴋ ᴘᴇʀᴍɪꜱꜱɪᴏɴ, ᴄᴜʀʀᴇɴᴛ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ ᴠᴀʟᴜᴇ: {FORCE_SUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nʙᴏᴛ ꜱᴛᴏᴘᴘᴇᴅ. ᴊᴏɪɴ https://t.me/HRBsupport ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛ")
                sys.exit()
        
        
       
     
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"ᴍᴀᴋᴇ ꜱᴜʀᴇ ʙᴏᴛ ɪꜱ ᴀᴅᴍɪɴ ɪɴ ᴅʙ ᴄʜᴀɴɴᴇʟ, ᴀɴᴅ ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ CHANNEL_ID ᴠᴀʟᴜᴇ, ᴄᴜʀʀᴇɴᴛ ᴠᴀʟᴜᴇ {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nʙᴏᴛ ꜱᴛᴏᴘᴘᴇᴅ. ᴊᴏɪɴ https://t.me/HRBsupport ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛ")
            sys.exit()

         initadmin = await full_adminbase()
        for x in initadmin:
            if x in ADMINS:
                continue
            ADMINS.append(x)
        await self.send_message(
            chat_id=OWNER_ID,
            text="Bot has started! 😉"
        )

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/HRBsupport")
        self.LOGGER(__name__).info(f"""\n\n


██╗░░██╗██████╗░██████╗░
██║░░██║██╔══██╗██╔══██╗
███████║██████╔╝██████╦╝
██╔══██║██╔══██╗██╔══██╗
██║░░██║██║░░██║██████╦╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
                                        \n\n""")


        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
            
