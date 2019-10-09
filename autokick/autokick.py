import asyncio
import io
import aiohttp
import re

from collections import namedtuple

import discord
from redbot.core import Config, checks, commands
from redbot.core.utils.chat_formatting import box, pagify

# Don't join the furry channel

BaseCog = getattr(commands, "Cog", object)

channel_id = 502108640530923520

class AutoKick(BaseCog):
    """Furry is bad"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=974374573)
        default_guild = {}
        self.config.register_guild(**default_guild)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if (after.voice.voice_channel.id == channel_id):
            await after.member.id.move_to(channel=None, reason="No Furries Allowed")