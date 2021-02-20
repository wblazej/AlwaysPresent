import discord
from lib.config import Config

async def send_error(ctx, error: str):
    """
    This function sends an error information
    """
    
    embed = discord.Embed()
    embed.color = Config.ERROR_COLOR
    embed.description = error

    await ctx.send(embed=embed)