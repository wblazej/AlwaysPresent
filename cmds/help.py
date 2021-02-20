import discord
from discord.ext import commands
from os import listdir
import importlib

# libs
from lib.config import Config
from lib.parse_args import parse_args
from lib.command_help import command_help

class help(commands.Cog):
    """
    This function sends all commands and them 
    descriptions as embed message
    """

    def __init__(self, bot):
        self.bot = bot

    # COMMAND HELP PARSER DATA
    command = "help"
    aliases = ["pomoc"]
    arguments = [
        {"arg": "-h", "description": Config.HELP_ARGUMENT_DESCRIPTION}, 
        {"arg": "--help", "description": Config.HELP_ARGUMENT_DESCRIPTION}
    ]
    description = Config.HELP_COMMAND_DESCRIPTION
    example = None

    @commands.command(name=command, aliases=aliases)
    async def _help(self, ctx, *args):
        args = parse_args(args)

        if args.get("help") or args.get("h"):
            await command_help(ctx, help)
            return None
        
        content = ""
        for file in listdir("cmds"):
            if '.py' in file:
                name = file.replace('.py', '')
                command_file = importlib.import_module(f'cmds.{name}')
                command = getattr(command_file, name)

                content += f"» **{Config.PREFIX}{command.command}** - {command.description}\n"

        content += f"\n{Config.HELP_INFO}"

        embed = discord.Embed()
        embed.color = Config.MAIN_COLOR
        embed.title = "**POMOC**"
        embed.description = content
        embed.set_thumbnail(url=Config.INFO_ICON)
        await ctx.send(embed=embed)

# set up an extension
def setup(bot):
    bot.add_cog(help(bot))