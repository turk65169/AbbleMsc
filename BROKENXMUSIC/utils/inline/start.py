from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
from BROKENXMUSIC.plugins.bot.repo import start
import config
from BROKENXMUSIC import app


def start_panel(_):
    support_chat = config.SUPPORT_CHAT if config.SUPPORT_CHAT else f"https://t.me/{app.username}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=support_chat),
        ],
    ]
    return buttons


def private_panel(_):
    support_channel = config.SUPPORT_CHANNEL if config.SUPPORT_CHANNEL else f"https://t.me/{app.username}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"), 
            InlineKeyboardButton(text=_["S_B_7"], callback_data="repo_callback"),   
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_5"], url=support_channel),
        ],
     ]
    return buttons
    
@app.on_callback_query(filters.regex("repo_callback"))
async def repo_callback(client, callback_query):
    message = callback_query.message
    await start(client, message)  
    await callback_query.answer()

