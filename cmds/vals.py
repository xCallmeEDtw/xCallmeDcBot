import discord
import Modules.vals as find
from discord.ext import commands
from core.classes import Cog_Extension

class StatsEmbed:
	def __init__(self, msg, AllStats):
		embed=discord.Embed(title="General player stats")
		embed.set_author(name=msg, url=AllStats["link"], icon_url=AllStats["icon"])
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Valorant_logo_-_pink_color_version.svg/1200px-Valorant_logo_-_pink_color_version.svg.png")
		embed.add_field(name='K/D/A', value= f'Kills: {AllStats.get("Kills")} Deaths: {AllStats.get("Deaths")} Assists {AllStats.get("Assists")} K/D: {AllStats.get("K/D")} ', inline=False)
		embed.add_field(name="Wins", value=f'Won: {AllStats.get("Wins")} Win%: {AllStats.get("Win%")}', inline=True)
		embed.add_field(name="Stats", value=f'Headshots: {AllStats.get("Headshots")}', inline=True)
		embed.add_field(name="Extras", value=f'First Bloods: {AllStats.get("First Bloods")} Most Kills: {AllStats.get("Most Kills (Match)")} ', inline=False)
	    
	    # embed.add_reaction(message, '⏮')
	    # embed.add_reaction(message, '◀')
	    # embed.add_reaction(message, '▶')
	    # embed.add_reaction(message, '⏭')	
		self.embed = embed


class vals(Cog_Extension):
	@commands.group(pass_context=True)
	async def val(self, ctx):
		pass
	@val.group(pass_context=True)
	async def unrated(self, ctx):
		pass
	@unrated.command(pass_context=True, name='stats')
	async def unrated_stats(self, ctx,msg):
		AllStats = find.unrated.stats(msg)
		GetEmbed = StatsEmbed(msg, AllStats)
		await ctx.send(embed= GetEmbed.embed)
		print(ctx.message)
		await ctx.message.add_reaction("👍")
		#await ctx.add_reaction("<:noice:726803987185009011")
	    #await message.add_reaction('⏮')
	    # await message.add_reaction('◀')
	    # await message.add_reaction('▶')
	    # await message.add_reaction('⏭')

	@val.group(pass_context=True)
	async def competitive(self, ctx):
		pass
	@competitive.command(pass_context=True, name='stats')
	async def competitive_stats(self, ctx,msg):
		AllStats = find.competitive.stats(msg)
		GetEmbed = StatsEmbed(msg, AllStats)
		embed = GetEmbed.embed
		embed.add_field(name="Rank", value=f'Rank: {AllStats.get("rank")} ', inline=False)
		await ctx.send(embed= embed)

def setup(client):
	client.add_cog(vals(client))