# coding: utf-8

def computePrefixArray(patternArray):
	
	temp=[0]* len(patternArray)
	i=1
	j=0

	while i<len(patternArray):
		if patternArray[i]== patternArray[j]:
			j=j+1
			temp[i]=j
			i=i+1
		else:
			if j==0:
				temp[i]=0
				i=i+1
			else:
				j= temp[j-1]

	return temp

def getMatchesWithPattern(textArray,patternArray):

	temp=computePrefixArray( patternArray )
	i=0
	j=0

	for i in range(len(textArray)):
		if patternArray[j]==textArray[i]:
			j=j+1
			i=i+1
		else:
			if j!=0:
				j=temp[j-1]
			else:
				i=i+1
    
		if j==len(patternArray):
			posArray.append(i-j)
			print "Match Found at",i-j
			j=0	
	return posArray


def findCount(textArray,patternCollection):

	postArray=[]
	for p in range(len(patternCollection)):
		patternArray = list(patternCollection[p])
		postArray= getMatchesWithPattern( textArray, patternCollection[p])

	return postArray

def plotHistogram(positionArray):

	import collections
	positions=collections.Counter(positionArray)

	positionArray = list(set(positionArray))

	import matplotlib.pyplot as plt
	plt.xlabel("Position")
	plt.ylabel("Frequency")
	plt.title("Read count Histogram")
	for i in range(len(positionArray)):
		plt.bar(positionArray[i],positions.get(positionArray[i]), width=0.5)


	plt.show()

	
import sys

obj=-1

try:
    obj= open("genome.txt")
except IOError:
    print "File genome.txt not Found"
    sys.exit(0)

filecontent= obj.readline()

if filecontent=="":
	sys.exit(0)

textArray= list(filecontent)

f=-1

try:
    f= open("read.txt")
except IOError:
    print "File read.txt not Found"
    sys.exit(0)

content = f.read().splitlines()

if len(content)==0:
	 sys.exit(0)

patternArray = []
posArray= []

plotHistogram( findCount( textArray, content ))

