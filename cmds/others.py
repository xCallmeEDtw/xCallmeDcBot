import discord
from time import sleep
from discord.ext import commands
from core.classes import Cog_Extension
class others(Cog_Extension):
	@commands.command(pass_context=True)
	async def ping(self, ctx):
	    await ctx.send(f"{round(self.client.latency*1000)}(ms)")

	@commands.command(pass_context=True)
	async def say(self, ctx, *, msg):
		await ctx.message.delete()
		print(msg)
		await ctx.send(msg)
	@commands.command(pass_context=True)
	async def clean(self, ctx, num: int):
		await ctx.channel.purge(limit=num+1)
		await ctx.send(f"已清除{num}則訊息")
		sleep(2)
		await ctx.channel.purge(limit=1)


	@commands.command(pass_context=True)
	@commands.is_owner()
	async def shutdown(self, ctx):
	    await ctx.bot.logout()

  		

def setup(client):
	client.add_cog(others(client))
