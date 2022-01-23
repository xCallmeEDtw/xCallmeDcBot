import discord
from discord.ext import commands
from core.classes import Cog_Extension
class auto(Cog_Extension):
	@commands.Cog.listener() 
	async def on_ready(self):
		print(">>online<<")
	@commands.Cog.listener()
	async def on_member_join(self, member):
		for channels in member.guild.channels:
			if "一般" in str(channels):
				channel_id = channels.id
		#channel_id = 686184051769606170
		channel = self.client.get_channel(channel_id)
		await channel.send(f"{member.mention} Ahoy!~")

	@commands.Cog.listener() 
	async def on_member_remove(self, member):
		for channels in member.guild.channels:
			if "一般" in str(channels):
				channel_id = channels.id
		#channel_id = 686184051769606170
		channel = self.client.get_channel(channel_id)
		await channel.send(f"{member.mention} Bye~")
	@commands.Cog.listener()
	async def on_reaction_add(self, reaction, user):
		print(user)
		print(reaction)
def setup(client):
	client.add_cog(auto(client))