import discord
import Modules.games
from discord.ext import commands
from core.classes import Cog_Extension




class guess(Cog_Extension):

	@commands.group(pass_context=True, name='2A2B')
	async def myguess(self, ctx):
		pass

	@myguess.command(pass_context=True, name='try')
	async def mytry(self, ctx,msg):
		games = Modules.games 
		myreply = games.guess.answer(msg)
		await ctx.send(myreply)
	@myguess.command(pass_context=True)
	async def generate(self, ctx):
		games = Modules.games 
		games.guess.generate()
		await ctx.send("已重新生成一組數字")
	# @myguess.command(pass_context=True)
	# async def answer(self, ctx):
	# 	games = Modules.games 
	# 	games.guess.generate()
	# 	await ctx.send("已重新生成一組數字")






def setup(client):
	client.add_cog(guess(client))