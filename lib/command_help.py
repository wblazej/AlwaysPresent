from lib.config import Config
import discord

async def command_help(ctx, command_class):
    embed = discord.Embed()
    embed.color = Config.MAIN_COLOR
    embed.title = f"**{Config.PREFIX}{command_class.command}**"
    embed.add_field(name=Config.TRANSLATION_DESCRIPTION, value=command_class.description.capitalize(), inline=True)
    embed.set_thumbnail(url=Config.INFO_ICON)

    if len(command_class.aliases) > 0:
        aliases_content = ""
        for i in range(len(command_class.aliases)):
            aliases_content += f"{Config.PREFIX}{command_class.aliases[i]}"
            if i + 1 < len(command_class.aliases):
                aliases_content += ", "
        embed.add_field(name=Config.TRANSLATION_ALIASES, value=aliases_content, inline=True)

    if len(command_class.arguments) > 0:
        arguments_content = ""
        for arg in command_class.arguments:
            arguments_content += f"**{arg['arg']}** - {arg['description']}\n"
        embed.add_field(name=Config.TRANSLATION_ARGUMENTS, value=arguments_content, inline=False)


    await ctx.send(embed=embed)