import discord
from datetime import datetime
from datetime import timedelta
from math import floor
import pytz

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

        tz = pytz.timezone('Europe/Warsaw')
        self.started = datetime.now(tz).timestamp()

        embed = self.generate_embed()
        channel = self.bot.get_channel(self.channel)

        if not self.no_mention:
            await channel.send("@here")

        msg = await channel.send(embed=embed)
        await msg.add_reaction(Config.PRESENCE_EMOJI)

        self.msg_id = msg.id
        return self.msg_id

    async def check(self, user_id: int):
        if self.time_left() > 0:
            self.students.append(user_id)
            await self.reload()

    async def uncheck(self, user_id: int):
        if self.time_left() > 0:
            self.students.pop(self.students.index(user_id))
            await self.reload()

    async def reload(self):
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
            end_time = datetime.fromtimestamp(self.started + (60 * self.time))
            hour = end_time.hour
            minute = end_time.minute
            if hour < 10: hour = f"0{hour}"
            if minute < 10: minute = f"0{minute}"
            content += f"{Config.TRANSLATION_LESSON_END} **{hour}:{minute}**\n"

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

    def time_left(self):
        tz = pytz.timezone('Europe/Warsaw')
        return (self.started + (60 * self.time)) - datetime.now(tz).timestamp()