import discord
from discord.ext import commands

# libs
from lib.config import Config
from lib.parse_args import parse_args
from lib.command_help import command_help

class _bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # COMMAND HELP PARSER DATA
    command = "bot"
    aliases = ["b"]
    arguments = [
        {"arg": "-h", "description": Config.HELP_ARGUMENT_DESCRIPTION}, 
        {"arg": "--help", "description": Config.HELP_ARGUMENT_DESCRIPTION}
    ]
    description = Config.BOT_COMMAND_DESCRIPTION
    example = None

    @commands.command(name=command, aliases=aliases)
    async def _bot_(self, ctx, *args):
        args = parse_args(args)

        if args.get("help") or args.get("h"):
            await command_help(ctx, _bot)
            return None

        embed = discord.Embed()
        embed.title = Config.TRANSLATION_BOT_INFO
        embed.description = Config.BOT_DESCRIPTION
        embed.color = Config.MAIN_COLOR
        embed.set_thumbnail(url=Config.BOT_ICON)

        embed.add_field(name=Config.TRNASLATION_VERSION, value=Config.VERSION, inline=True)
        embed.add_field(name=Config.TRANSLATION_LANGUAGE, value=Config.LANGUAGE, inline=True)
        embed.add_field(name=Config.TRANSLATION_LIBRARY, value=Config.LIBRARY, inline=True)
        embed.add_field(name=Config.TRANSLATION_RUNNING_ON, value=Config.RUNNING_ON, inline=True)
        embed.add_field(name=Config.TRANSLATION_AUTHOR, value=Config.AUTHOR, inline=True)
        embed.add_field(name=Config.TRANSLATION_REPOSITORY, value=Config.REPO, inline=True)

        await ctx.send(embed=embed)

# set up an extension
def setup(bot):
    bot.add_cog(_bot(bot))