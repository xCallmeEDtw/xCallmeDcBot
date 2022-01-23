import requests as req
from bs4 import BeautifulSoup as mBS
def getData(selecter,tags):
	return  mBS(str(selecter.select(tags)[0]),'html.parser').text.translate({ord("\n" ): None})
class stats:
	def __init__(self, text):
		web = f'https://apex.tracker.gg/apex/profile/origin/{text}/overview'
		self.web = web
		r = req.get(web)
		soup = mBS(r.text, 'html.parser')
		cards = soup.select('.value')
		self.levels = cards[0].text
		self.kills = cards[1].text
		self.icon = (soup.select('img.ph-avatar__image'))[0]["src"]

	# winpers = getData(soup, '[data-stat="PVPWLRatio"]')
	# kills = getData(soup, '[data-stat="PVPKills"]')
	# KD = getData(soup, '[data-stat="PVPKDRatio"]')
	
def operater(player,operator):
	op_id ={
	'kali': '[data-index="2:17"]'
	
	}
	web = f'https://r6.tracker.network/profile/pc/{player}/operators'

	r = req.get(web)

	soup = mBS(r.text, 'html.parser')

	myreply = soup.select(op_id.get(operator))[0].text.split()

	print('played time:',myreply[1],myreply[2])
	print('kills:',myreply[3])
	print('KD:',myreply[4])
	print('WINS:',myreply[5])
	print('Lossers:',myreply[6])
	print('你媽勝負比:',myreply[7])
	
	return(myreply)
