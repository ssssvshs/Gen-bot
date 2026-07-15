import discord
import random
import os

# Load codes from the file
with open("bulk_year_2017_1784091848070.txt", "r") as f:
    code_list = [line.strip() for line in f if line.strip()]

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Loaded {len(code_list)} codes.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("!generate"):
        if not code_list:
            await message.channel.send("No codes available.")
            return
        # Pick a random code
        code = random.choice(code_list)
        await message.channel.send(code)

bot.run(TOKEN)