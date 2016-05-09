import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help, settings
import aiohttp
import asyncio
import os
import logging
import json

class Post:
	"""Post's a playlist or cog in chat."""

	def __init__(self,bot):
		self.bot = bot

	@commands.command(no_pm=True, pass_context=True)
	@checks.admin_or_permissions(kick_members=True)
	async def postsongs(self, ctx, *, playlist):
		"""Posts a playlist"""

		file = fileIO("data/audio/playlists/"+ctx.message.server.id+"/"+playlist+".txt","load")
		await self.bot.say(file["link"])

	@commands.command(no_pm=True, pass_context=True)
	@checks.is_owner()
	async def postcog(self, ctx, *, cog):
		"""Posts a Cog"""

		await self.bot.send_file(ctx.message.channel, 'cogs/'+cog+'.py')

def setup(bot):
	n = Post(bot)
	bot.add_cog(n)