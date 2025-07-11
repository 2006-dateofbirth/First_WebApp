import operator

def count(article):
    words = article.split()
    word_count = len(words)
    dict_words = {}

    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    sorted_words = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_words, word_count
