from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import math
import spacy

nlp = spacy.load('en_core_web_lg')


def home(request):
    return render(request, 'home.html')

    
def count(request):
    fulltext = request.POST['fulltext']

    doc = nlp(fulltext)

    lst_entities = []
    lst_ent = []
    set_lst_entities = set()
    most_common_words = []

    
    words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
    len_text = len(doc)
    word_freq = Counter(words)
    common_words = word_freq.most_common(5)
    # most_common_words = [k[0] for k in common_words]
    # most_common_words_count = [k[1] for k in common_words]
    for k in common_words:
        most_common_words.append(k[0])
        most_common_words.append(k[1])

    print("common_words", common_words)
    # print("most_common_words_count", most_common_words_count)
    
    if doc.ents:
        for ent in doc.ents:

            if ent.text in common_words[0]:
                text = ent.text
                # lst_ent.append(text)
                if text not in set_lst_entities:
                    lst_entities.append(text)
                    set_lst_entities.add(text)
                else:
                    pass

    val = math.ceil(len_text/200) * 60

    if val < 60:
        unit = 'second(s)'
        val = val
    elif val >= 60 and val < 3600:
        unit = 'minute(s)'
        val = val/60
    elif val >= 3600:
        unit = 'hour(s)'
        val = val/3600

    return render(request, 'home.html', {'count':len_text, \
                'mostfrqwords':common_words, \
                'time':val, 'unit': unit, 'fulltext': doc, \
                'lst_entities': lst_entities})