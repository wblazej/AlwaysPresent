import discord
from discord.ext import commands
from decouple import config
import decouple
from os import listdir

# libs
from lib.config import Config
from lib.error import send_error
from lib.format_date import get_formated_warsaw_datetime
from lib.logging import Logging

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=Config.PREFIX, intents=intents)
bot.remove_command('help')

if __name__ == "__main__":
    print("Loading...")

    for file in listdir("cmds"):
        if file.split('.')[-1] == "py":
            name = file.replace('.py', '')
            bot.load_extension(f"cmds.{name}")

@bot.event
async def on_ready():
    print("\n==============================\n")
    print(f'{bot.user.name} logged in succesfully')
    print(f'Discord.py: v{discord.__version__}')
    print(f'{bot.user.name} bot: v{Config.VERSION}')
    print("\n==============================\n")

    await bot.change_presence(activity=discord.Game(name="&help"))

# handle errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await send_error(ctx, Config.UNKNOWN_COMMAND) # command not found error
    elif isinstance(error, commands.errors.MissingPermissions):
        await send_error(ctx, Config.MISSING_PERMISSIONS) # mising permissions error
    elif isinstance(error, commands.errors.NoPrivateMessage):
        await send_error(ctx, Config.SERVER_COMMAND) # execute guild command in dm error
    elif isinstance(error, commands.errors.CommandInvokeError):
        if type(error.original) == discord.errors.Forbidden:
            await send_error(ctx, Config.WRONG_CONFIG) # bot has no permissions to do something
        else:
            raise error
    else:
        raise error

@bot.event
async def on_command(ctx):
    username = ctx.author.display_name
    guild_name = ctx.guild.name
    command = ctx.message.content
    date = get_formated_warsaw_datetime()

    Logging.info(f"User \033[1m{username}\033[0m executed command \033[1m{command}\033[0m on server \033[1m{guild_name}\033[0m | ({date})")

try:
    bot.run(config("TOKEN"), bot=True, reconnect=True)
except decouple.UndefinedValueError:
    Logging.error(f"Token hasn't been provided in file \033[1m.env\033[0m")