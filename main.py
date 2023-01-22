import discord
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "proof" in message.content or "prove" in message.content:
        await message.reply("https://i.imgur.com/hm9ZOk1.gif")


client.run(os.getenv("DISCORD_TOKEN"))
