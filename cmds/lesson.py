import discord
from discord.ext import commands
from lib.discord_emojis import DiscordEmojis

# libs
from lib.parse_args import parse_args
from lib.command_help import command_help
from lib.config import Config
from lib.error import send_error
from lib.lesson import Lesson

lessons = dict()

class lesson(commands.Cog):
    """
    This function starts lesson on text channel and
    takes informations about presence on lessons by message reactions
    """

    def __init__(self, bot):
        self.bot = bot

    # COMMAND HELP PARSER DATA
    command = "lesson"
    aliases = ["lekcja", "l"]
    arguments = [
        {"arg": "-h", "description": Config.HELP_ARGUMENT_DESCRIPTION}, 
        {"arg": "--help", "description": Config.HELP_ARGUMENT_DESCRIPTION},
        {"arg": "-t <minutes>", "description": Config.TIME_ARGUMENT_DESCRIPTION}, 
        {"arg": "--time <minutes>", "description": Config.TIME_ARGUMENT_DESCRIPTION},
        {"arg": "-p", "description": Config.PRACTICE_ARGUMENT_DESCRIPION}, 
        {"arg": "--practice", "description": Config.PRACTICE_ARGUMENT_DESCRIPION},
        {"arg": "-n", "description": Config.NO_MENTION_ARG_DESCRIPTION}, 
        {"arg": "--no-mention", "description": Config.NO_MENTION_ARG_DESCRIPTION}
    ]
    description = Config.LESSON_COMMAND_DESCRIPTION
    example = Config.LESSON_COMMAND_EXAMPLE

    @commands.command(name=command, aliases=aliases)
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def _lesson(self, ctx, *args):
        args = parse_args(args)

        if args.get("help") or args.get("h"):
            await command_help(ctx, lesson)
            return

        time = None
        if args.get("time"):
            time = args['time']['value']
        elif args.get("t"):
            time = args['t']['value']

        if time:
            try:
                time = int(time)
            except ValueError:
                await send_error(ctx, Config.TIME_INTEGER_REQIURED)
                return

        practice = False
        if args.get("practice") or args.get("p"):
            practice = True

        no_mention = False
        if args.get("no-mention") or args.get("n"):
            no_mention = True

        await ctx.message.delete()

        new_lesson = Lesson(bot=self.bot,
                            teacher=ctx.author.id,
                            channel=ctx.channel.id,
                            guild=ctx.guild.id,
                            time=time,
                            practice=practice,
                            no_mention=no_mention)

        lessons[await new_lesson.begin_lesson()] = new_lesson
        
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return

        if reaction.message.id in lessons.keys():
            await lessons[reaction.message.id].check(user.id)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user.bot:
            return

        if reaction.message.id in lessons.keys():
            await lessons[reaction.message.id].uncheck(user.id)

# set up an extension
def setup(bot):
    bot.add_cog(lesson(bot))