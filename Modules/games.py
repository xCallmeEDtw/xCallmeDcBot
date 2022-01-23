import random
def mora(text):
	con = ['剪刀' ,'石頭','布']
	result = ['You win~', "平手", '哈，輸了吧廢物']
	if text == con[0]:
		text =0
	elif text == con[1]:
		text = 1
	elif text == con[2]:
		text = 2
	myran = random.randint(0,2)
	if myran == text:
		myreply = result[1]
	elif (text == 0 and myran == 2) or (text == 1 and myran == 0) or (text == 2 and myran == 1):
		myreply = result[0]
	else:
		myreply = result[2]
	return [con[myran],myreply]
class guess:
	def generate():
		myNum = ""
		while len(myNum) <4:
			r = str(random.randint(0,9))
			if not(r in myNum):
				myNum += r
		file = open('2A2B.txt',mode='w')
		file.write(myNum)
		file.close()
	def answer(text):
		file = open('2A2B.txt',mode='r')
		myNum = file.read()
		file.close() 
		cntA = 0
		cntB = 0

		for i in range(len(text)):
			if text[i] == myNum[i]:
				cntA += 1
			elif text[i] in myNum:
				cntB += 1
		return(f"{cntA}A {cntB}B")

