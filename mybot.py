import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send(f"yes ma'am/sir")

    elif isinstance(message.channel, discord.TextChannel):
        await message.channel.send(f"yes ma'am/sir")

    await bot.process_commands(message)

@bot.tree.command(name="ping", description="Responds with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@bot.command()
async def sync(ctx):
    await bot.tree.sync()
    await ctx.send("sync done!")
bot.run('your token')
