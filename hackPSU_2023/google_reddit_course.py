from googlesearch import search

def search_bar(query):
    return query


def results(query):
    lst=[]
    for j in search(query, tld="co.in", num=5, stop=5, pause=2):
        lst+=[j]
    return lst

