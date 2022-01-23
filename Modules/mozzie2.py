import requests as req
from bs4 import BeautifulSoup as mBS
def getData(selecter,tags):
	return  mBS(str(selecter.select(tags)[0]),'html.parser').text.translate({ord("\n" ): None})
def r6_states(text):

	web = f'https://r6.tracker.network/profile/pc/{text}'

	r = req.get(web)

	soup = mBS(r.text, 'html.parser')

	wins = getData(soup,'[data-stat="PVPMatchesWon"]')
	winpers = getData(soup, '[data-stat="PVPWLRatio"]')
	kills = getData(soup, '[data-stat="PVPKills"]')
	KD = getData(soup, '[data-stat="PVPKDRatio"]')
	
	return(kills,KD,wins,winpers)
def r6_operater(player,operator):
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
def val_states(text):
	name = text.split("#")
	#kami#3153
	web = f'https://tracker.gg/valorant/profile/riot/{name[0]}%23{name[1]}/overview'
	r = req.get(web)
	print('2')
	print(r.status_code)
	print('3')
	try:
		soup = mBS(r.text, 'html.parser')
		cards = (soup.select('.main'))
		stats = cards[0].text.split()
		cards = (soup.select('[data-v-5edf1b22], .value'))
		stats2 = ""
		for i in range(3,len(cards),9):
			stats2 += (cards[i].text)
		stats2 = stats2.split()
		myreply = [stats[1],stats2[10],stats[3],stats2[4],stats[5],stats[18]]
		return(myreply)
	# for i in range(len(stats)):
	#  	print()
	except:
		return("查無此人")	


