from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import ReplyKeyboardRemove

video_url = 'https://graph.org/file/0bdb84af27036dd3561e1.mp4'
dev = InlineKeyboardButton("丂丨几丂", url=f"https://t.me/D_3_V")

subs = InlineKeyboardMarkup(
        [
            [
                dev,
            ],
        ]
    )