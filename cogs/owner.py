"""
Misc commands that I want to run
"""

import discord
from discord.ext import commands
from.utils import checks


class Owner():
    """
    Cog with misc owner commands
    """

    def __init__(self, bot):
        """
        init for cog class
        """
        super().__init__()
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def add_server(self, ctx):
        """
        Adds a server to the db
        """
        try:
            await self.bot.postgres_controller.add_server(ctx.guild.id)
            self.bot.server_settings[ctx.guild.id] = {
                'prefix': '-',
                'modlog_enabled': False
            }
            await ctx.send('\N{OK HAND SIGN}', delete_after=3)
            await ctx.message.delete()
        except Exception as e:
            await ctx.send('❌', delete_after=3)
            self.bot.logger.warning(f'Error adding server to db: {e}')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def echo(self, ctx, channel, *, message):
        """
        Echoes a string into a different channel
        :params channel: channel to echo into
        :params message: message to echo
        """
        if not ctx.message.channel_mentions:
            return await ctx.send(
                f'<command> <channel mention> <message> u idiot')
        try:
            for channel in ctx.message.channel_mentions:
                await channel.send(f'{message}')
        except Exception as e:
            ctx.send('Error when trying to send fam')
