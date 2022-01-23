import requests as req
from bs4 import BeautifulSoup as mBS
def getData(selecter,tags):
	return  mBS(str(selecter.select(tags)[0]),'html.parser').text.translate({ord("\n" ): None})
def if_num(word):
	if '%' in word:
		word = word[:-1]
	if ',' in word:
		word = word.translate({ord("," ): None})
	try:
		word = float(word)
	except:
		return(False)
	return(True)
def stats(text):
	StatsDict= {}
	new = []
	web = f'https://r6.tracker.network/profile/pc/{text}'

	r = req.get(web)

	soup = mBS(r.text, 'html.parser')
	cards = (soup.select('.trn-defstats--width4'))[2]
	for card in cards:
		try:
			temp = (card.text)
			temps = temp[1:].split("\n")
			StatsDict[temps[0]] = temps[2]

		except:
			pass
	StatsDict["link"] = web
	#print(cards[2])

	StatsDict["Kills"] = getData(soup, '[data-stat="PVPKills"]')
	#= getData(soup,'[data-stat="PVPMatchesWon"]')
	# winpers = getData(soup, '[data-stat="PVPWLRatio"]')
	# kills = getData(soup, '[data-stat="PVPKills"]')
	# KD = getData(soup, '[data-stat="PVPKDRatio"]')
	StatsDict
	return(StatsDict)
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
