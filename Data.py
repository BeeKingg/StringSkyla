from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝗛𝗔𝗟𝗟𝗢 {}

𝗦𝗲𝗹𝗮𝗺𝗮𝘁 𝗗𝗮𝘁𝗮𝗻𝗴 {}
━━━━━━━━━━━━━━━━━━━━━━━━
𝗝𝗶𝗸𝗮 𝗸𝗮𝗺𝘂 𝘁𝗶𝗱𝗮𝗸 𝗽𝗲𝗿𝗰𝗮𝘆𝗮 𝗱𝗲𝗻𝗴𝗮𝗻 𝗯𝗼𝘁 𝗶𝗻𝗶:
1. 𝗝𝗮𝗻𝗴𝗮𝗻 𝗱𝗶𝗯𝗮𝗰𝗮 𝗽𝗲𝘀𝗮𝗻 𝗶𝗻𝗶
2. 𝗕𝗹𝗼𝗸𝗶𝗿 𝗱𝗮𝗻 𝗵𝗮𝗽𝘂𝘀 𝗯𝗼𝘁 𝗶𝗻𝗶
━━━━━━━━━━━━━━━━━━━━━━━━
𝗕𝗼𝘁 𝗶𝗻𝗶 𝗕𝗲𝗸𝗲𝗿𝗷𝗮 𝗨𝗻𝘁𝘂𝗸 𝗠𝗲𝗺𝗯𝗮𝗻𝘁𝘂 𝗞𝗮𝗺𝘂 𝗠𝗲𝗻𝗱𝗮𝗽𝗮𝘁𝗸𝗮𝗻 𝗦𝘁𝗿𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗗𝗲𝗻𝗴𝗮𝗻 𝗠𝘂𝗱𝗮𝗵!
━━━━━━━━━━━━━━━━━━━━━━━━
𝗠𝗮𝗻𝗮𝗴𝗲𝗱 𝗪𝗶𝘁𝗵 ☕️ 𝗕𝘆 @Zxyune
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("☕ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ☕", callback_data="generate")],
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("☕ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ☕", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("☕ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ☕", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ", url="https://t.me/Zxyune")],
        [
            InlineKeyboardButton("ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ ❔", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ɪɴғᴏ ʙᴏᴛ ʟᴀɪɴ", url="https://t.me/skylasupport")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @StringSkylaBot

Group Support : [ɢᴀʙᴜɴɢ](https://t.me/skylasupport)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Zxyune
    """
