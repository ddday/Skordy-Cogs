import discord
from discord.ext import commands
import aiohttp
from .utils import checks

class Resolver:
    """Ping Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, pass_context=True)
    @checks.is_owner()
    async def nping(self, ctx, user_input: str):
        """Check to see if a website is responsive."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/nping/?q="+user_input) as resp:
            await self.bot.say("```diff\n" + await resp.text() + "```")

    @commands.command(no_pm=True, pass_context=True)
    @checks.is_owner()
    async def mtr(self, ctx, user_input: str):
        """Checks the routing of a hostname or IP."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/mtr/?q="+user_input) as resp:
            await self.bot.say("" + await resp.text())

    @commands.command(no_pm=True, pass_context=True)
    @checks.is_owner()
    async def geoip(self, ctx, user_input: str):
        """Checks the location of an IP."""
		
        async with aiohttp.request('GET', "http://api.hackertarget.com/geoip/?q="+user_input) as resp:
            await self.bot.say("The location of that IP is:\n" + await resp.text())

    @commands.command(no_pm=True, pass_context=True)
    async def upordown(self, ctx, user_input: str):
        """Checks to see if a website is online or not."""

        async with aiohttp.request('GET', "http://api.predator.wtf/upordown/?arguments="+user_input) as resp:
            await self.bot.say("" + await resp.text())
			
    @commands.command(no_pm=True, pass_context=True)
    @checks.is_owner()
    async def dnslookup(self, ctx, user_input: str):
        """Checks the DNS records of a hostname."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/dnslookup/?q="+user_input) as resp:
            await self.bot.say("" + await resp.text())
			
    @commands.command(no_pm=True, pass_context=True)
    @checks.is_owner()
    async def reversedns(self, ctx, user_input: str):
        """Checks the DNS hostname."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/reversedns/?q="+user_input) as resp:
            await self.bot.say("" + await resp.text())
			
    @commands.command(no_pm=True, pass_context=True)
    @checks.is_owner()
    async def headers(self, ctx, user_input: str):
        """Returns header information of a hostname."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/httpheaders/?q="+user_input) as resp:
            await self.bot.say("" + await resp.text())
			
    @commands.command(no_pm=True, pass_context=True)
    @checks.is_owner()
    async def pagelinks(self, ctx, user_input: str):
        """Displays all the links within a web page."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/pagelinks/?q="+user_input) as resp:
            await self.bot.say("" + await resp.text())

def setup(bot):
    n = Resolver(bot)
    bot.add_cog(n)