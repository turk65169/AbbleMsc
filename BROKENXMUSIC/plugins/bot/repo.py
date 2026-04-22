from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from BROKENXMUSIC import app
import config

status_text = """
🍏 **Apple Music Bot - Hizmet Durumu** 🍏

**Sistem Durumu:** `✅ Aktif ve Kesintisiz Çevrimiçi`
**Bağlantı Gecikmesi:** `Sıfır Gecikme (Low Latency)`
**Desteklenen Platformlar:** `YouTube, Spotify, SoundCloud, Apple Music`

*Bot kesintisiz bir müzik ziyafeti yaşamanız için optimize edilmiş, özel sunucularda yüksek kaliteli ses kodekleri ile barındırılmaktadır.*
"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
            InlineKeyboardButton(text="💬 Destek Topluluğu", url=config.SUPPORT_CHAT if config.SUPPORT_CHAT else f"https://t.me/{app.username}"),
            InlineKeyboardButton(text="📣 Duyurular", url=config.SUPPORT_CHANNEL if config.SUPPORT_CHANNEL else f"https://t.me/{app.username}")
        ]
    ]
    await msg.reply_text(
        text=status_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )
