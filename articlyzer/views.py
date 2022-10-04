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
abcdef = nltk.download('averaged_perceptron_tagger')
nltk_words = nltk.download('words')
sr = stopwords.words('english')
sr.append('.')


def home(request):
    return render(request, 'home.html')


def count(request):
    article_content = '' if request.POST.get('article_content') is None else request.POST.get('article_content')
    # doc = nlp(article_content)

    # lst_entities = []
    # lst_ent = []
    # set_lst_entities = set()
    # most_common_words = []

    # words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
    tokens = nltk.word_tokenize(article_content)
    total_words_count = len(tokens)

    clean_tokens = tokens[:]

    for token in tokens:
        if token in sr:
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)
    frequent_words = freq.most_common(5)
    tagged = nltk.pos_tag(tokens)
    token_ent = nltk.ne_chunk(tagged, binary=True)

    # for key, value in freq.most_common(5):
    #     print(u'{}:{}'.format(key, value))
    #     most_common_words.append(key)
    #     most_common_words.append(value)

    # total_words_count = len(doc)

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

    time_to_read = (total_words_count / 200) * 60

    if time_to_read < 60:
        time_unit = 'second'
        time_to_read = time_to_read
    elif 60 <= time_to_read < 3600:
        time_unit = 'minute'
        time_to_read = time_to_read / 60
    elif time_to_read >= 3600:
        time_unit = 'hour'
        time_to_read = time_to_read / 3600

    return render(
        request,
        'home.html',
        {
            'total_words_count': total_words_count,
            'time_to_read': round(time_to_read),
            'time_unit': time_unit + 's' if time_to_read > 1 else time_unit,
            'article_content': article_content,
            'frequent_words': frequent_words
        }
    )
