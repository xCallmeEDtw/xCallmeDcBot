import discord
import Modules.r6s as find
from discord.ext import commands
from core.classes import Cog_Extension

def StatsEmbed(msg, AllStats):

	embed=discord.Embed(title="General player stats")
	#embed.set_author(name=msg, url=AllStats["link"], icon_url=AllStats["icon"])
	embed.set_thumbnail(url="https://wallpapercave.com/wp/wp5631995.jpg")
	embed.add_field(name='Kill/Death', value= f'Kills: {AllStats.get("Kills")} Deaths: {AllStats.get("Deaths")}  K/D: {AllStats.get("KD")} ', inline=False)
	embed.add_field(name="Wins", value=f'Won: {AllStats.get("Wins")} Win%: {AllStats.get("Win %")} Losses:{AllStats.get("Losses")}', inline=True)
	embed.add_field(name="Stats", value=f'Headshots: {AllStats.get("Headshots")} Matches Played: {AllStats.get("Matches Played")} Time Played: {AllStats.get("Time Played")}' , inline=True)
	embed.add_field(name="Extras", value=f'Blind Kills: {AllStats.get("Blind Kills")} Melee Kills: {AllStats.get("Melee Kills")} ', inline=False)
	return embed


class r6s(Cog_Extension):
	@commands.group(pass_context=True)
	async def r6(self, ctx):
		pass

	@r6.command(pass_context=True, name='stats')
	async def stats(self, ctx,msg):
		AllStats = find.stats(msg)
		embed = StatsEmbed(msg, AllStats)
		await ctx.send(embed= embed)

	# @r6.command(pass_context=True, name='stats')
	# async def competitive_stats(self, ctx,msg):
	# 	AllStats = find.competitive.stats(msg)
	# 	GetEmbed = StatsEmbed(msg, AllStats)
	# 	embed = GetEmbed.embed
	# 	embed.add_field(name="Rank", value=f'Rank: {AllStats.get("rank")} ', inline=False)
	# 	await ctx.send(embed= embed)

def setup(client):
	client.add_cog(r6s(client))