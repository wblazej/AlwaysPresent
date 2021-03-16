import discord
from discord.ext import commands

# libs
from lib.parse_args import parse_args
from lib.command_help import command_help
from lib.config import Config
from lib.error import send_error
from lib.questionnaire import Questionnaire

questionnaires = dict()

class question(commands.Cog):
    """
    This function creates a questionaire with
    live results on text channel
    """

    def __init__(self, bot):
        self.bot = bot

    # COMMAND HELP PARSER DATA
    command = "question"
    aliases = ["pytanie", "ankieta", "q"]
    arguments = [
        {"arg": "-h", "description": Config.HELP_ARGUMENT_DESCRIPTION}, 
        {"arg": "--help", "description": Config.HELP_ARGUMENT_DESCRIPTION},
        {"arg": "-q <question>", "description": Config.QUESTION_ARGUMENT_DESCRIPTION}, 
        {"arg": "--question <question>", "description": Config.QUESTION_ARGUMENT_DESCRIPTION},
        {"arg": "-a1 <answer>", "description": Config.HELP_ARGUMENT_DESCRIPTION}, 
        {"arg": "--answer1 <answer>", "description": Config.HELP_ARGUMENT_DESCRIPTION}
    ]
    description = Config.QUESTION_COMMAND_DESCRIPTION
    example = Config.QUESTION_COMMAND_EXAMPLE

    @commands.command(name=command, aliases=aliases)
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def _question(self, ctx, *args):
        args = parse_args(args)

        if args.get("help") or args.get("h"):
            await command_help(ctx, question)
            return
        
        __question = None
        if args.get('q'):
            __question = args['q']
        elif args.get('question'):
            __question = args['question']
        if __question:
            __question = __question.get("value")

        answers = []
        i = 1
        while True:
            a = None
            if args.get(f"a{i}"):
                a = args[f"a{i}"]
            elif args.get(f"answer{i}"):
                a = args[f"answer{i}"]
            if a:
                if a.get("value"):
                    answers.append(a['value'])
            else:
                break
            i += 1

        if not __question:
            await send_error(ctx, Config.NO_QUESTION)
            return

        if len(answers) < 2:
            await send_error(ctx, Config.TWO_ANSWERS_REQUIRED)
            return

        if len(answers) > 9:
            await send_error(ctx, Config.MAX_NINE_ANSWERS)
            return

        content = ''
        for i in range(len(answers)):
            content += f'{Config.DISCORD_EMOJIS_NUMBERS[i]} {answers[i]}\n'

        content += Config.CHOOSE_ANSWER

        await ctx.message.delete()

        embed = discord.Embed()
        embed.color = Config.MAIN_COLOR
        embed.title = f"**{__question}**"
        embed.description = content
        embed.set_thumbnail(url=Config.QUESTION_ICON)
        msg = await ctx.send(embed=embed)

        result_msg = await ctx.send(self.generate_result_content([0]*len(answers)))
        questionnaires[msg.id] = Questionnaire([0]*len(answers), ctx.channel.id, result_msg.id)

        for i in range(len(answers)):
            await msg.add_reaction(Config.DISCORD_EMOJIS_NUMBERS_UNICODE[i])
        
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        await self.vote_changed(reaction=reaction, user=user, status="add")

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        await self.vote_changed(reaction=reaction, user=user, status="remove")

    async def vote_changed(self, reaction, user, status):
        if user.bot:
            return

        msg_id = reaction.message.id

        if msg_id in questionnaires.keys():
            try:
                if status == "add":
                    questionnaires[msg_id].answers_count[int(reaction.emoji[:1]) - 1] += 1
                elif status == "remove":
                    questionnaires[msg_id].answers_count[int(reaction.emoji[:1]) - 1] -= 1

                new_msg_content = self.generate_result_content(questionnaires[msg_id].answers_count)

                channel = self.bot.get_channel(questionnaires[msg_id].channel_id)
                msg = await channel.fetch_message(questionnaires[msg_id].result_msg_id)
                await msg.edit(content=new_msg_content)
            except ValueError:
                await reaction.remove(user)

    def generate_result_content(self, answers_count):
        content = f'**Odpowiedzi: {sum(answers_count)}**\n'

        for i in range(len(answers_count)):
            content += f'{Config.DISCORD_EMOJIS_NUMBERS[i]} '

            try:
                persentage = round(answers_count[i] / sum(answers_count) * 100, 2)
            except ZeroDivisionError:
                persentage = 0

            blocks = round(persentage / 10)

            for _ in range(blocks):
                content += '▉'
            content += f' **{persentage}%**\n'

        return content

# set up an extension
def setup(bot):
    bot.add_cog(question(bot))