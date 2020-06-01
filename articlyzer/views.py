from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import math
import spacy

nlp = spacy.load('en_core_web_lg')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def count(request):
    fulltext = request.POST['fulltext']

    doc = nlp(fulltext)
    print('doc :', doc)

    wordlist = fulltext.split()

    worddict = {}
    l = []
    cntr = 0
    total_count = 0
    lst_entities = []
    lst_ent = []
    set_lst_entities = set()

    for word in wordlist:
        total_count += 1
        if nlp.vocab[word].is_stop == False:
            if word in worddict:
                #Increase the counter
                worddict[word] += 1
                cntr+=1
            else:
                #add to dictionary
                worddict[word] = 1
                cntr+=1
        else:
            pass
    
    if doc.ents:
        for ent in doc.ents:
            text = ent.text
            lst_ent.append(text)
            label = ent.label_
            lst_ent.append(label)
            explain = str(spacy.explain(ent.label_))
            lst_ent.append(explain)
            if text not in set_lst_entities:
                lst_entities.append(lst_ent)
                set_lst_entities.add(text)
            else:
                pass
            lst_ent = []

    k = Counter(worddict)
    high = k.most_common(3)
    for items in high:
        l.append(items[0])

    mfw = ', '.join(l)
    val = math.ceil(total_count/200)

    if val > 1:
        unit = 'minutes'
    else:
        unit = 'minute'

    return render(request, 'home.html', {'count':len(wordlist), \
                'mostfrqwords':mfw, 'time':val, 'unit': unit, 'fulltext': fulltext, \
                'lst_entities': lst_entities})
                # 'text': text, 'label': label, 'explain': explain})