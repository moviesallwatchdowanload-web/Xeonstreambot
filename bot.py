import os
from pyrogram import Client, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8804089517:AAHqd76DTwoegs_M2IXaz0FMAkLRw1u92dw")
API_ID = int(os.environ.get("API_ID", "1234567"))
API_HASH = os.environ.get("API_HASH", "your_api_hash_here")

app = Client(
    "XeonStreamBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("👋 Namaste! Main Xeon Stream Bot hoon. Mujhe file bhejiye!")

@app.on_message(filters.document | filters.video | filters.audio)
async def file_handler(client, message):
    file = message.video or message.document or message.audio
    file_name = file.file_name if file else "Media File"
    await message.reply(f"✅ File mil gayi: `{file_name}`")

if __name__ == "__main__":
    app.run()
