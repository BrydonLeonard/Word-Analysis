import re
import sys

yourName = "Brydon Leonard"

list = ''
listYou = ''

f = open(sys.argv[1], encoding='utf-8')

for line in f:
	try:
		list += (re.sub('[^A-Za-z ]+', '', re.sub('^.+(?=-)-.+(?=:): ', '', line)).replace('<Media omitted>','').replace('\n',' ')+' ')
		listYou += re.sub('[^A-Za-z ]+', '', re.sub('(^(?!.+'+yourName+').+)|(^.+(?=-)-.+?(?=:))|(.*Media omitted.*)','', line)).replace('\n',' ')+' '
	except:
		pass



def countingSortAndDisp(dataArr, labelArr, isYou):
	if isYou == 1:
		outputF = open(sys.argv[2]+'1way.csv','w')
	else:
		outputF = open(sys.argv[2]+'.csv', 'w')
	max = 0
	for i in dataArr:
		if i > max:
			max = i

	tempData = []
	tempLabel = []

	for i in range(0,max+1):
		tempData.append([])
		tempLabel.append([])

	for i in range(0, len(dataArr)):
		if not labelArr[i] in [' ', '']:
			tempLabel[dataArr[i]].append(labelArr[i])

	for i in range(1, len(tempLabel)+1):
		for j in range(0, len(tempLabel[len(tempLabel)-i])):
			try:
				outputF.write(tempLabel[len(tempLabel)-i][j] +',' + str(len(tempLabel)-i)+"\n")
			except:
				pass





arr = list.lower().split(' ')
freq = []
words = []
for item in arr:
	if not item in words:
		freq.append(1)
		words.append(item)
	else:
		freq[words.index(item)] += 1
countingSortAndDisp(freq, words,0)

arr = listYou.lower().split(' ')
freq = []
words = []
for item in arr:
	if not item in words:
		freq.append(1)
		words.append(item)
	else:
		freq[words.index(item)] += 1
countingSortAndDisp(freq, words, 1)
