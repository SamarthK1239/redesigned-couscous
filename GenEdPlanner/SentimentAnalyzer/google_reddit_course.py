from googlesearch import search

def search_bar(query):
    return query


def results(query):
    lst=[]
    for j in search(query, tld="co.in", num=3, stop=3, pause=1.5):
        lst+=[j]
    return lst

