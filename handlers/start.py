import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""👋 Hai {message.from_user.mention()} 

Saya adalah [{bn}](t.me/{bu}), bot yang bisa streaming musik di OS/VCG !
jangan sungkan tambahkan saya ke grup kalian ya...

Jika kalian punya pertanyaan atau masalah lainnya?
kalian bisa hubungi ➥ [Owner](t.me/punyaa_ra)

**Kalian ingin berdonasi? boleh pake bangettt**

[Donasi](https://bit.ly/idoganz) - [Join Channel](t.me/Idoganz_Project) - [Command List](https://telegra.ph/COMMAND-LIST-06-10)

Ingin Menambahkan Saya ke Grup Anda? Cukup Klik Tombol di Bawah""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    "➕ ᴛᴀᴍʙᴀʜᴋᴀɴ ꜱᴀʏᴀ ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ", url=f"https://t.me/{bu}?startgroup=true"
                    ),
                ],[
                    InlineKeyboardButton(
                        "👤 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/punyaa_ta"
                    ),
                    InlineKeyboardButton(
                        "📥 ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘ", url=f"https://t.me/{Idoganzzbot}"
                    )
                ],[
                    InlineKeyboardButton(
                        "➥ ɪɴʟɪɴᴇ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "📺 ʏᴏᴜᴛᴜʙᴇ", url="https://youtube.com/c/dhimasazman"
                    )
                ],[
                    InlineKeyboardButton(
                        "📝 ʀᴇᴘᴏꜱɪᴛᴏʀʏ", url=f"https://github.com/mr494/Jooxmusic"
                    ),
                ]
            ]
       ),
    )

