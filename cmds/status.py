import discord
from discord.ext import commands

# libs
from lib.config import Config
from lib.parse_args import parse_args
from lib.command_help import command_help
from lib.error import send_error

class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # COMMAND HELP PARSER DATA
    command = "status"
    aliases = []
    arguments = [
        {"arg": "-h", "description": Config.HELP_ARGUMENT_DESCRIPTION}, 
        {"arg": "--help", "description": Config.HELP_ARGUMENT_DESCRIPTION},
        {"arg": "-s <status>", "description": Config.STATUS_ARGUMENT_DESCRIPTION},
        {"arg": "--status <status>", "description": Config.STATUS_ARGUMENT_DESCRIPTION},
        {"arg": "-r", "description": Config.REMOVE_ARGUMENT_DESCRIPTION},
        {"arg": "--remove", "description": Config.REMOVE_ARGUMENT_DESCRIPTION}
    ]
    description = Config.STATUS_COMMAND_DESCRIPTION
    example = None

    @commands.command(name=command, aliases=aliases)
    async def _status_(self, ctx, *args):
        args = parse_args(args)

        if args.get("help") or args.get("h"):
            return await command_help(ctx, status)

        if args.get("status") or args.get("s"):
            print(ctx.message.author.id)
            if ctx.message.author.id != Config.ADMIN_ID:
                return await send_error(ctx, "Brak uprawnień")

            new_status = args["status"].get("value") if args.get("status") else args["s"].get("value")

            if not new_status:
                return await send_error(ctx, "Podaj nowy status")
                
            await self.bot.change_presence(activity=discord.Game(name=new_status))
            return await ctx.channel.send(":white_check_mark: Ustawiono nowy status")

        if args.get("remove") or args.get("r"):
            if ctx.message.author.id != Config.ADMIN_ID:
                return await send_error(ctx, "Brak uprawnień")

            await self.bot.change_presence(activity=discord.Game(name=f"{Config.PREFIX}help"))
            return await ctx.channel.send(":white_check_mark: Usunięto status")

        await command_help(ctx, status)

# set up an extension
def setup(bot):
    bot.add_cog(status(bot))