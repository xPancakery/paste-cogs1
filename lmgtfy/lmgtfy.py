import discord
import re
from redbot.core import commands
from .split import split_into_sentences


class lmgtfy(commands.Cog):
    """
    Redbot cog that takes a message and makes a 'lmgtfy' link out of it.

    .lmgtfy "<question>"
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lmgtfy(self, ctx: commands.Context, question):
        """
        **Wrap your <question> in DOUBLE cum QUOTES**
        """
        
        for i in split_into_sentences(self, question):
            if 'app/?' not in i[0:5]:
                if 'q=' not in i[0:2]:
                    o = re.split(r'\s|(?<!\d)[\?](?!\d)/gm', i)
                    output = "https://lmgtfy.app/?q="
                    for l in o:
                        output = ''.join([output, l+'+'])
                    output = output[:-1]
                    await ctx.send(output)
                else:
                    return ("I can't seem to find a question.")
