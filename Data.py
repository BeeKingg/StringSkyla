from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
๐๐๐๐๐ข {}

๐ฆ๐ฒ๐น๐ฎ๐บ๐ฎ๐ ๐๐ฎ๐๐ฎ๐ป๐ด {}
โโโโโโโโโโโโโโโโโโโโโโโโ
๐๐ถ๐ธ๐ฎ ๐ธ๐ฎ๐บ๐ ๐๐ถ๐ฑ๐ฎ๐ธ ๐ฝ๐ฒ๐ฟ๐ฐ๐ฎ๐๐ฎ ๐ฑ๐ฒ๐ป๐ด๐ฎ๐ป ๐ฏ๐ผ๐ ๐ถ๐ป๐ถ:
1. ๐๐ฎ๐ป๐ด๐ฎ๐ป ๐ฑ๐ถ๐ฏ๐ฎ๐ฐ๐ฎ ๐ฝ๐ฒ๐๐ฎ๐ป ๐ถ๐ป๐ถ
2. ๐๐น๐ผ๐ธ๐ถ๐ฟ ๐ฑ๐ฎ๐ป ๐ต๐ฎ๐ฝ๐๐ ๐ฏ๐ผ๐ ๐ถ๐ป๐ถ
โโโโโโโโโโโโโโโโโโโโโโโโ
๐๐ผ๐ ๐ถ๐ป๐ถ ๐๐ฒ๐ธ๐ฒ๐ฟ๐ท๐ฎ ๐จ๐ป๐๐๐ธ ๐ ๐ฒ๐บ๐ฏ๐ฎ๐ป๐๐ ๐๐ฎ๐บ๐ ๐ ๐ฒ๐ป๐ฑ๐ฎ๐ฝ๐ฎ๐๐ธ๐ฎ๐ป ๐ฆ๐๐ฟ๐ถ๐ป๐ด ๐ฆ๐ฒ๐๐๐ถ๐ผ๐ป ๐๐ฒ๐ป๐ด๐ฎ๐ป ๐ ๐๐ฑ๐ฎ๐ต!
โโโโโโโโโโโโโโโโโโโโโโโโ
๐ ๐ฎ๐ป๐ฎ๐ด๐ฒ๐ฑ ๐ช๐ถ๐๐ต โ๏ธ ๐๐ @Zxyune
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("โ sแดแดสแด ษขแดษดแดสแดแดษชษดษข sแดssษชแดษด โ", callback_data="generate")],
        [InlineKeyboardButton(text="แดแดแดสแดสษช", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("โ sแดแดสแด ษขแดษดแดสแดแดษชษดษข sแดssษชแดษด โ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("โ sแดแดสแด ษขแดษดแดสแดแดษชษดษข sแดssษชแดษด โ", callback_data="generate")],
        [InlineKeyboardButton("แดแดษชษดแดแดษดแดแด สส", url="https://t.me/Zxyune")],
        [
            InlineKeyboardButton("แดแดสแด แดแดษดษขษขแดษดแดแดแดษด sแดสแด โ", callback_data="help"),
            InlineKeyboardButton("แดสแดแดแด", callback_data="about")
        ],
        [InlineKeyboardButton("ษชษดาแด สแดแด สแดษชษด", url="https://t.me/skylasupport")],
    ]

    # Help Message
    HELP = """
โจ **Available Commands** โจ

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

Group Support : [ษขแดสแดษดษข](https://t.me/skylasupport)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Zxyune
    """
