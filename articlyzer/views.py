from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import math
# import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

abc = nltk.download('wordnet')
abcd = nltk.download('stopwords')
abcde = nltk.download('punkt')
# abcdef = nltk.download('averaged_perceptron_tagger')
# nlp = spacy.load('en_core_web_sm')
sr = stopwords.words('english')
sr.append('.')


def home(request):
    return render(request, 'home.html')

    
def count(request):
    fulltext = request.POST['fulltext']

    # doc = nlp(fulltext)

    # lst_entities = []
    # lst_ent = []
    # set_lst_entities = set()
    # most_common_words = []

    
    # words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
    tokens = nltk.word_tokenize(fulltext)
    len_text = len(tokens)

    clean_tokens = tokens[:]

    for token in tokens:
        if token in sr:
            print('token------->', token)
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)
    freq_cmn = freq.most_common(5)
    tagged = nltk.pos_tag(tokens)
    token_ent = nltk.ne_chunk(tagged, binary=True)

    # for key, value in freq.most_common(5):
    #     print(u'{}:{}'.format(key, value))
    #     most_common_words.append(key)
    #     most_common_words.append(value)

    # len_text = len(doc)

    print('fulltext------->', fulltext)
    print('token_ent------>', token_ent)
    print('len_text------->', len_text)
    print('clean_tokens------->', clean_tokens)
    print('tokens------->', tokens)
    print('freq_cmn------->', freq_cmn)
    

    # word_freq = Counter(words)
    # common_words = word_freq.most_common(5)
    # most_common_words = [k[0] for k in common_words]
    # # most_common_words_count = [k[1] for k in common_words]
    # for k in common_words:
    #     most_common_words.append(k[0])
    #     most_common_words.append(k[1])

    # print("common_words", common_words)
    # # print("most_common_words_count", most_common_words_count)
    
    # if doc.ents:
    #     for ent in doc.ents:

    #         if ent.text in common_words[0]:
    #             text = ent.text
    #             # lst_ent.append(text)
    #             if text not in set_lst_entities:
    #                 lst_entities.append(text)
    #                 set_lst_entities.add(text)
    #             else:
    #                 pass

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
                'time':val, 'unit': unit, 'fulltext': fulltext, \
                'mostfrqwords': freq_cmn})