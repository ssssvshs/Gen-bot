import discord
import random
import string
import os   # <-- This lets the bot read the token from Railway

# ---------- Generate code ----------
def generate_code():
    left_len = random.randint(12, 20)
    left = ''.join(random.choices(string.ascii_letters + string.digits, k=left_len))
    right_len = random.randint(5, 8)
    right = ''.join(random.choices(string.ascii_letters + string.digits, k=right_len))
    return f"{left}:ALTGEN{right}"

# ---------- Discord Bot ----------
TOKEN = os.getenv('TOKEN')  # Reads the token from Railway's settings

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("!generate"):
        code = generate_code()
        await message.channel.send(code)

bot.run(TOKEN)