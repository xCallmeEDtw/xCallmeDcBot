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
def ReOrg(mylist):
	new = []
	temp = ""
	mydict = {}
	for i in range(len(mylist)):
		if if_num(mylist[i]):
			new.append(temp)
			new.append(mylist[i])
			temp = ""
		else:
			temp += (mylist[i] + " ")
	for i in range(len(new)):
		if not(if_num(new[i])):
			new[i] = new[i][:-1]
	for i in range(0,len(new)-1,2):
		mydict[new[i]] = new[i+1] 



	return(mydict)
def stats_temp( name,web):

	# self.name = name
	# #kami#3153
	# self.web = web
	r = req.get(web)
	#print(r.status_code)
	soup = mBS(r.text, 'html.parser')
	cards = (soup.select('.main'))
	stats = cards[0].text.split()
	cards = (soup.select('span [data-v-5edf1b22], .value'))
	stats2 = []
	for i in range(len(cards)):
		stats2.append(cards[i].text)
	stats2 = stats2[3:7]
	img = (soup.select('image'))[0]["href"]
	#print(img)
	rank = soup.select('.valorant-highlighted-stat__value')[0].text
	#print(rank)
	StatsDict = ReOrg(stats)
	StatsDict["K/D"] = stats2[1]
	StatsDict["Win%"] = stats2[-1]
	StatsDict["link"] = web
	StatsDict["icon"] = img
	StatsDict["rank"] = rank
	# self.soup = soup
	# self.StatsDict = StatsDict
	return(StatsDict)

class unrated:
	def stats(text):
 		name = text.split("#")
 		web = f'https://tracker.gg/valorant/profile/riot/{name[0]}%23{name[1]}/overview?playlist=unrated'
 		StatsDict = stats_temp(name, web)
 		return(StatsDict)

class competitive:
	def stats(text):
 		name = text.split("#")

 		web = f'https://tracker.gg/valorant/profile/riot/{name[0]}%23{name[1]}/overview?playlist=competitive'
 		StatsDict = stats_temp(name, web)
 		return(StatsDict)