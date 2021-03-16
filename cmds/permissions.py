import discord
from discord.ext import commands
from lib.discord_emojis import DiscordEmojis

# libs
from lib.parse_args import parse_args
from lib.command_help import command_help
from lib.config import Config
from lib.error import send_error

class permissions(commands.Cog):
    """
    This function displays all permissions that bot needs
    to work properly
    """

    def __init__(self, bot):
        self.bot = bot

    # COMMAND HELP PARSER DATA
    command = "permissions"
    aliases = ["uprawnienia", "p"]
    arguments = [
        {"arg": "-h", "description": Config.HELP_ARGUMENT_DESCRIPTION}, 
        {"arg": "--help", "description": Config.HELP_ARGUMENT_DESCRIPTION}
    ]
    description = Config.PERMISSIONS_COMMAND_DESCRIPTION
    example = None

    @commands.command(name=command, aliases=aliases)
    async def _permissions(self, ctx, *args):
        args = parse_args(args)

        if args.get("help") or args.get("h"):
            await command_help(ctx, permissions)
            return

        embed = discord.Embed()
        embed.color = Config.MAIN_COLOR
        embed.title = Config.TRANSLATION_PERMISSIONS
        embed.set_thumbnail(url=Config.PERMISSIONS_ICON)

        content = f"{Config.TRANSLATION_PERMISSIONS_CODE}: {Config.PERMISSIONS_CODE}\n\n"

        for permission in Config.PERMISSIONS_LIST:
            content += f":white_check_mark: {permission}\n"

        embed.description = content
        await ctx.send(embed=embed)        

# set up an extension
def setup(bot):
    bot.add_cog(permissions(bot))