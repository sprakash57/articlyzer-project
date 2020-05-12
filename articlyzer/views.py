from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import math


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def count(request):
    fulltext = request.POST['fulltext']

    wordlist = fulltext.split()

    worddict = {}
    l = []
    cntr = 0

    for word in wordlist:
        if word in worddict:
            #Increase the counter
            worddict[word] += 1
            cntr+=1
        else:
            #add to dictionary
            worddict[word] = 1
            cntr+=1

    k = Counter(worddict)
    high = k.most_common(3)
    for items in high:
        l.append(items[0])

    mfw = ', '.join(l)
    val = math.ceil(cntr/200)

    if val > 1:
        unit = 'minutes'
    else:
        unit = 'minute'

    return render(request, 'home.html', {'count':len(wordlist), 'mostfrqwords':mfw, 'time':val, 'unit': unit, 'fulltext': fulltext})