import discord
import random
import os
from discord.ext import commands
from core.classes import Cog_Extension
from Modules import games
class msgs(Cog_Extension):
	@commands.Cog.listener()
	async def on_message(self, message):
		path = './Picture/choose'
		files = os.listdir(path)
		#id = client.get_quild(686184051261833251 )
		con = ['剪刀' ,'石頭','布' ]
		SplitText = message.content.split()
		print(message.content)
		# print(message.content.find("123"))
		if message.author != self.client.user:
			if message.content.find("121") != -1:
				await message.channel.send('123')
			elif  message.content in con:
				myreply = games.mora(message.content)
				await message.channel.send(myreply[0])
				await message.channel.send(myreply[1])
			
			elif message.content == "抽":
				RanPic = f"./Picture/choose/{random.choice(files)}"
				print(RanPic)
				pic = discord.File(RanPic)
				await message.channel.send(file = pic)
		#await self.client.process_commands(message)
def setup(client):
	client.add_cog(msgs(client))

	# elif SplitText != []:

	# 		elif SplitText[0] == '$r6' and len(SplitText) >= 3:
	# 			if SplitText[1] == 'stats':
	# 				myreply = r6_states(SplitText[2])
	# 				await message.channel.send("Kills: " + myreply[0])
	# 				await message.channel.send("KD: " + myreply[1])	
	# 				await message.channel.send("Wins: " + myreply[2])
	# 				await message.channel.send("Win%: " + myreply[3])

	# 			elif SplitText[1] == 'operater' and len(SplitText) == 4:
	# 				myreply = r6_operater(SplitText[2],SplitText[3])
	# 				await message.channel.send('played time:' + myreply[1] +' '+myreply[2] )
	# 				await message.channel.send('kills:' + myreply[3] + ' KD:'+ myreply[4])
	# 				await message.channel.send('WINS:' + myreply[5] + ' Lossers:' + myreply[6])
	# 				await message.channel.send('Wins%:'+ myreply[7])
	# 				await message.channel.send('幹員特殊道具成功使用'+ myreply[-1] )