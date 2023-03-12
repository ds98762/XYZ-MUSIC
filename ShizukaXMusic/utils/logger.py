from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from ShizukaXMusic.utils.database import is_on_off
from ShizukaXMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**💞 {MUSIC_BOT_NAME} ᴍᴜsɪᴄ ʟᴏɢs **
**━━━━━━━━━━━━━━━**
**🌹️ 𝙲𝙷𝙰𝚃 𝙽𝙰𝙼𝙴 : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**🥀 𝙽𝙰𝙼𝙴 : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**🌸 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**🌷 𝚄𝚂𝙴𝚁 𝙸𝙳  : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**🌿 𝙲𝙷𝙰𝚃 𝙻𝙸𝙽𝙺 : >** {chatusername}
**━━━━━━━━━━━━━━━**
**🌻 𝚂𝙴𝙰𝚁𝙲𝙷𝙴𝙳 𝙵𝙾𝚁 : >** {message.text}
**━━━━━━━━━━━━━━━**
**💐 𝚂𝚃𝚁𝙴𝙰𝙼 𝚃𝚈𝙿𝙴 : >** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
