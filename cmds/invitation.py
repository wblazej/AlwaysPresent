import discord
from discord.ext import commands
from os import listdir
import importlib

# libs
from lib.config import Config
from lib.parse_args import parse_args
from lib.command_help import command_help

class invitation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    command = "invitation"
    aliases = ["zaproszenie", "inv"]
    arguments = [
        {"arg": "-h", "description": Config.HELP_ARGUMENT_DESCRIPTION}, 
        {"arg": "--help", "description": Config.HELP_ARGUMENT_DESCRIPTION}
    ]
    description = Config.INVITATION_COMMAND_DESCRIPTION

    @commands.command(name=command, aliases=aliases)
    async def _invite(self, ctx, *args):
        args = parse_args(args)

        if args.get("help") or args.get("h"):
            await command_help(ctx, invitation)
            return None

        embed = discord.Embed()
        embed.title = Config.TRANSLATION_INVITATION
        embed.description = Config.INVITATION
        embed.color = Config.MAIN_COLOR
        embed.set_thumbnail(url=Config.INVITATION_ICON)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(invitation(bot))