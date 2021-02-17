import discord
from discord.ext import commands
from lib.discord_emojis import DiscordEmojis

# libs
from lib.parse_args import parse_args
from lib.command_help import command_help
from lib.config import Config
from lib.error import send_error
from lib.questionnaire import Questionnaire

# variable that stores all data about questions
questionnaires = dict()

class question(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
            content += f'{DiscordEmojis.numbers[i]} {answers[i]}\n'

        content += Config.CHOOSE_ANSWER

        await ctx.message.delete()

        embed = discord.Embed()
        embed.color = Config.MAIN_COLOR
        embed.title = f"**{__question}**"
        embed.description = content
        msg = await ctx.send(embed=embed)

        result_msg = await ctx.send(question.generate_result_content([0]*len(answers)))
        questionnaires[msg.id] = Questionnaire(__question, answers, [0]*len(answers), ctx.channel.id, result_msg.id)

        for i in range(len(answers)):
            await msg.add_reaction(DiscordEmojis.numbers_unicode[i])
        

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return

        msg_id = reaction.message.id

        stop = False
        if msg_id in questions.keys():
            try:
                questions[msg_id]['answers_count'][int(reaction.emoji[:1]) - 1] += 1
            except ValueError:
                await reaction.remove(user)
                stop = True

            if stop == False and questions[msg_id].get('result_msg_id') != None:
                new_msg_content = question.generate_result_content(questions[msg_id]['answers_count'])

                channel = self.bot.get_channel(questions[msg_id]['channel_id'])
                msg = await channel.fetch_message(questions[msg_id]['result_msg_id'])
                await msg.edit(content=new_msg_content)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user.bot:
            return

        msg_id = reaction.message.id

        stop = False
        if msg_id in questions.keys():
            try:
                questions[msg_id]['answers_count'][int(reaction.emoji[:1]) - 1] -= 1
            except ValueError:
                await reaction.remove(user)
                stop = True

            if stop == False and questions[msg_id].get('result_msg_id') != None:
                new_msg_content = question.generate_result_content(questions[msg_id]['answers_count'])

                channel = self.bot.get_channel(questions[msg_id]['channel_id'])
                msg = await channel.fetch_message(questions[msg_id]['result_msg_id'])
                await msg.edit(content=new_msg_content)

    def generate_result_content(answers_count):
        all_answers = sum(answers_count)
        content = f'**Odpowiedzi: {all_answers}**\n'

        for i in range(len(answers_count)):
            content += f'{DiscordEmojis.numbers[i]} '
            if all_answers > 0:
                persentage = round(answers_count[i] / all_answers * 100, 2)
            else: persentage = 0
            blocks = round(persentage / 10)
            for _ in range(blocks):
                content += '▉'
            content += f' **{persentage}%**\n'

        return content

# set up extension
def setup(bot):
    bot.add_cog(question(bot))