import discord
from dotenv import load_dotenv
import os
from discord.ext import tasks, commands
from datetime import datetime

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_message(message: discord.Message) -> None:
    if message.author == bot.user:
        return

    if any(
        [
            (x.startswith("prove") or x.startswith("proof"))
            for x in message.content.split(" ")
        ]
    ):
        if message.author.id == 207432575541575681:
            await message.reply("Stop memeing. Go do your proofs. Janicki is waiting.")
        else:
            await message.reply("https://i.imgur.com/hm9ZOk1.gif")

    if "moore" in message.content.lower():
        if message.author.id == 207432575541575681:
            await message.reply("Stop memeing. Go do your proofs. Janicki is waiting.")
        else:
            await message.reply("GET OUT OF MY OFFICE")
            await message.add_reaction("<:goToHell:1035735109174833172>")


class MyCog(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.quiz_reminder.start()

    def cog_unload(self):
        self.quiz_reminder.cancel()

    @tasks.loop(seconds=1.0)
    async def quiz_reminder(self):
        today = datetime.now()
        if today.weekday() == 0 and (
            today.hour == 0 and today.minute == 0 and today.second == 0
        ):
            await self.bot.get_channel(1056078158014726216).send(
                f"<@&1069731625946075187> Friendly reminder : Do your 2ac3 quiz please."
            )
        if today.weekday() == 0 and (
            today.hour == 11 and today.minute == 0 and today.second == 0
        ):
            await self.bot.get_channel(1056078158014726216).send(
                f"<@&1069731625946075187> Less Friendly reminder : Do your 2ac3 quiz."
            )
        if today.weekday() == 0 and (
            today.hour == 15 and today.minute == 30 and today.second == 0
        ):
            await self.bot.get_channel(1056078158014726216).send(
                f"<@&1069731625946075187> DO YOUR FUCKING QUIZ OR ELSE"
            )
        if today.weekday() == 0 and (
            today.hour == 19 and today.minute == 14 and today.second == 0
        ):
            print("send")
            await self.bot.get_channel(846922359625875457).send(
                f"<@&1069731625946075187> DO YOUR FUCKING QUIZ OR ELSE"
            )

    @quiz_reminder.before_loop
    async def before_printer(self):
        print("waiting...")
        await self.bot.wait_until_ready()


bot.add_cog(MyCog(bot))
bot.run(os.getenv("DISCORD_TOKEN"))
