import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
bot = commands.Bot(command_prefix="!", intents=intents)
resp = ["Pipong! 🏓", "Too slow, nouha said! 😎", "TAKE THIS ... PONG! 🔥", "don't waste my time loser ..."]
resp_sp = ["What now ??", "okey duuh", "Aye, aye, Captain!!"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send(random.choice(resp_sp))

    elif bot.user in message.mentions:
        await message.channel.send(random.choice(resp_sp))

    await bot.process_commands(message)

@bot.tree.command(name="ping", description="Responds with some creative pong...")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(resp))

@bot.command()
async def sync(ctx):
    await bot.tree.sync()
    await ctx.send("Dude ... sync is done!")
bot.run('TOKEN')
