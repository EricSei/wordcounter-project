from django.http import HttpResponse
from django.shortcuts import render
import operator 
def home(request):
	return render(request, 'home.html', {'HITHERE': 'This is me'})



def count(request):
	# fulltext pass from home.html
	fulltext = request.GET['fulltext']
	
	wordlist = fulltext.split()
	worddictionary = {}
	for word in wordlist:
		if word in worddictionary:
			#increase
			worddictionary[word]+=1
		else:
			#add to the dictionary
			worddictionary[word]=1

	sortedWords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True )
	return render(request, 'count.html', {'text': fulltext, 'count':len(wordlist), 'sortedWords':sortedWords}) 

def about(request):
	return render(request, 'about.html')