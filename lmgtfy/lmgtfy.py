import discord
import re
from redbot.core import commands
#v1.1.1
class lmgtfy(commands.Cog):
    """
    Redbot cog that takes a message and makes a 'lmgtfy' link out of it.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def google(self, ctx: commands.Context, question):
        """
        Wrap your <question> in **double quotes**
        """
        o = re.split(r'\s|(?<!\d)[\?](?!\d)/gm', question)
        output = "https://www.google.com/search?q="
        if len(o) > 1:
            for l in o:
                output = ''.join([output, l+'+'])
            output = output[:-1]
            await ctx.send(output)
        elif len(o) == 1:
            output = ''.join([output, question])
            await ctx.send(output)
        else:
            await ctx.send("Wrap your <question> in **double quotes**")

    @commands.command()
    async def lmgtfy(self, ctx: commands.Context, *question):
        """
        I can't seem to find a question to google?
        """
        o = re.split(r'\s|(?<!\d)[\?](?!\d)/gm', *question)
        output = "https://www.google.com/search?q="
        if len(o) > 1:
            for l in o:
                output = ''.join([output, l+'+'])
            output = output[:-1]
            await ctx.send(output)
        elif len(o) == 1:
            output = ''.join([output, *question])
            await ctx.send(output)