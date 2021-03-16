import discord
from datetime import datetime

# libs
from lib.config import Config
from lib.format_date import get_formated_warsaw_datetime
from lib.parse_nick import parse_nick

class Lesson:
    def __init__(self, bot, teacher: int, channel: int, guild: int, time: any = None, practice: bool = False, no_mention: bool = False):
        self.teacher = teacher
        self.channel = channel
        self.guild = guild
        self.time = time
        self.practice = practice
        self.no_mention = no_mention

        self.bot = bot

    async def begin_lesson(self):
        self.students = []
        self.started = datetime.now().timestamp()

        embed = self.generate_embed()
        channel = self.bot.get_channel(self.channel)

        if not self.no_mention:
            await channel.send("@here")

        msg = await channel.send(embed=embed)
        await msg.add_reaction(Config.PRESENCE_EMOJI)

        self.msg_id = msg.id
        return self.msg_id

    async def check(self, user_id: int):
        self.students.append(user_id)
        to_edit = await self.bot.get_channel(self.channel).fetch_message(self.msg_id)
        await to_edit.edit(embed=self.generate_embed())

    async def uncheck(self, user_id: int):
        self.students.pop(self.students.index(user_id))
        to_edit = await self.bot.get_channel(self.channel).fetch_message(self.msg_id)
        await to_edit.edit(embed=self.generate_embed())

    def generate_embed(self):
        embed = discord.Embed()

        if self.practice:
            embed.title = Config.TRANSLATION_PRACTICE
        else:
            embed.title = Config.TRANSLATION_LESSON

        embed.color = Config.MAIN_COLOR
        embed.set_thumbnail(url=Config.LESSON_ICON)

        content = f"{Config.TRANSLATION_STARTED} **{get_formated_warsaw_datetime()}**\n"

        teacher_dispaly_name = self.bot.get_guild(self.guild).get_member(self.teacher).display_name
        if self.practice:
            content += f"{Config.TRANSLATION_LEADER} **{teacher_dispaly_name}**\n"
        else:
            content += f"{Config.TRANSLATION_TEACHER} **{teacher_dispaly_name}**\n"

        if self.time:
            minutes_passed = round((datetime.now() - datetime.fromtimestamp(self.started)).total_seconds() / 60)
            minutes_left = self.time - minutes_passed

            if minutes_left <= 0:
                content += f"**{Config.TRANSLATION_LESSON_FINISHED}**"
            else:
                minutes_left_str = ""
                if minutes_left == 1: 
                    minutes_left_str = f"{minutes_left} {Config.TRANSLATION_MINUTE}"
                elif minutes_left > 1 and minutes_left < 5:
                    minutes_left_str = f"{minutes_left} {Config.TRANSLATION_MINUTES2}"
                else:
                    minutes_left_str = f"{minutes_left} {Config.TRANSLATION_MINUTES1}"

                content += f"{Config.TRANSLATION_LEFT} **{minutes_left_str}**\n"

        content += f"\n{Config.LESSON_PRESENCE_INFORMATION}\n"

        if len(self.students) > 0:
            content += f"\n**{Config.TRANSLATION_PRESENCE_LIST}**\n"

            names = []
            for student_id in self.students:
                parsing_result = parse_nick(self.bot.get_guild(self.guild).get_member(student_id).display_name)
                names.append(f"{parsing_result[1]} {parsing_result[0]}")

            names.sort()

            for i in range(len(names)):
                content += f"{i + 1}. {names[i]}\n"

        embed.description = content

        return embed