import discord
import Modules.apex as find
from discord.ext import commands
from core.classes import Cog_Extension

def StatsEmbed(msg,AllStats):

	embed=discord.Embed(title="General player stats")
	embed.set_author(name=msg, url= AllStats.web, icon_url=AllStats.icon)
	embed.set_thumbnail(url="https://toppng.com/uploads/preview/orillaz-apex-logo-11563052813el3dpir3aq.png")
	embed.add_field(name='normal', value= f'Kills: {AllStats.kills} Levels: {AllStats.levels} ', inline=False)

	return(embed)


class apexes(Cog_Extension):
	@commands.group(pass_context=True)
	async def apex(self, ctx):
		pass
	@apex.command(pass_context=True, name='stats')
	async def stats(self, ctx,msg):
		AllStats = find.stats(msg)
		GetEmbed = StatsEmbed(msg, AllStats)

		await ctx.send(embed= GetEmbed)
		#print(ctx.message)
		await ctx.message.add_reaction("👌")
		#await ctx.add_reaction("<:noice:726803987185009011")
	    #await message.add_reaction('⏮')
	    # await message.add_reaction('◀')
	    # await message.add_reaction('▶')
	    # await message.add_reaction('⏭')


def setup(client):
	client.add_cog(apexes(client))