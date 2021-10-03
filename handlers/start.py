from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/52c504595249a6199162d.jpg")
    await message.reply_text(
        f"""**Hey, I'm LOVELY MUSIC BOT🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Powered by [#𝙍𝙤𝙗𝙤 𝙉𝙚𝙩𝙬𝙤𝙧𝙠](https://t.me/ROBO_NETWORK)

Add me to your group and play music freely❣️!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📠 Source Code 📠", url="https://github.com/TEAM-LOVELY/MUSIC")
                  ],[
                    InlineKeyboardButton(
                        "⚜ SUPPORT GROUP ⚜", url="https://t.me/ISHQWALE"
                    ),
                    InlineKeyboardButton(
                        "🔷️ UPDATE CHANNEL 🔷️", url="https://t.me/ROBO_NETWORK"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ADD TO GROUP 🥺", url="https://t.me/@Doremon_VC_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**#𝙍𝙤𝙗𝙤 𝙉𝙚𝙩𝙬𝙤𝙧𝙠**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔷️ UPDATE CHANNEL 🔷️", url="https://t.me/ROBO_NETWORK")
                ]
            ]
        )
   )


