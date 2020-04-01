# Author: @CoolSpring8
# Date: 2020/03/31
# Generally following "How can you build a basic search engine on your own? - Jayesh Lalwani's answer - Quora"
# https://qr.ae/pNv9VX
# Note: This is somehow bound to be impractical, inefficient and not robust,
# as it is intended to be a very simple example and due to my ability.
import os


def analyze_data(file):
    '''
    raw_data.txt example:

    http://yummypizza.com - Italian Pizza
    http://yummierpizza.com - Sicilian Pizza
    http://sexyshoes.com - Italian Shoes

    '''
    with open(file) as f:
        dataTable = {line.split(
            ' - ')[0]: line.split(' - ')[1].rstrip() for line in f}
    invertedIndex = dict()
    for k, v in dataTable.items():
        for keyword in v.split():
            keyword = keyword.lower()
            if keyword in invertedIndex:
                invertedIndex[keyword].add(k)
            else:
                invertedIndex[keyword] = {k}
    return invertedIndex, dataTable


def simple_search(search_word, index, data):
    try:
        wordList = [word.lower() for word in search_word.split()]
        resultSet = set()
        wordList = replace_synonyms(wordList)
        wordList = remove_stopwords(wordList)
        for word in wordList:
            try:
                for url in index[word]:
                    resultSet.add(data[url] + '\n- ' + url)
            except KeyError:
                pass
        resultList = sort_results(resultSet, order='alphabetical')
        if resultList:
            return '\n'.join(resultList)
        else:
            return 'Nothing Found'
    except Exception:
        return 'Something goes wrong'


def replace_synonyms(word_list):
    # NTLK can be introduced to add some features, such as plural to singular
    SYNONYM = {'italy': 'italian'}
    for synonym, acceptedWord in SYNONYM.items():
        word_list = [acceptedWord if word ==
                     synonym else word for word in word_list]
    return word_list


def remove_stopwords(word_list):
    STOPWORD = {'i', 'want'}
    for stopword in STOPWORD:
        while True:
            try:
                word_list.remove(stopword)
            except ValueError:
                break
    return word_list


def sort_results(result_set, order):
    result_list = list(result_set)
    if order == 'alphabetical':
        result_list.sort()
    else:
        # Some other sorting stuff could be done here
        result_list.sort()
    return result_list


if __name__ == '__main__':
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    index, data = analyze_data(os.path.join(__location__, 'raw_data.txt'))
    while True:
        print(simple_search(
            input('Please type in what you want to search: '), index, data))
