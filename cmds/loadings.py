import discord
from discord.ext import commands
from core.classes import Cog_Extension
class loadings(Cog_Extension):
	@commands.command(pass_context=True)
	async def load(self, ctx ,extension):
		self.client.load_extension(f'{extension}')
		await ctx.send(f'Loaded {extension} done')
	@commands.command(pass_context=True)
	async def unload(self, ctx ,extension):
		self.client.unload_extension(f'{extension}')
		await ctx.send(f'unLoaded {extension} done')	 
	@commands.command(pass_context=True)
	async def reload(self, ctx ,extension):
		self.client.reload_extension(f'{extension}')
		await ctx.send(f'reLoaded {extension} done')

def setup(client):
	client.add_cog(loadings(client))
