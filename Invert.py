from typing import TextIO
from string import punctuation
import re
import pickle

def add_to_dictionary(x, d, s, doc_num, term_pos, post_list):
    temp_list = x.split()
    if len(s) > 0:
        for word in temp_list:
            if not(word in s):
                term = word.strip(punctuation)
                term = re.sub(r'[^\w\-]', '', term)
                if not (term.isspace() or len(term) < 1):
                    d[term] = d.get(term, 0) + 1
    else:
        for word in temp_list:
            term = word.strip(punctuation)
            term = re.sub(r'[^\w\-]', '', term)
            term = term.lower()
            if not(term.isspace() or len(term) < 1):
                d[term] = d.get(term, 0) + 1
                post_list = add_to_posting(term, doc_num, term_pos, post_list)
                term_pos += 1
    return d, term_pos, post_list

# need to add document frequency as well to list
def add_to_posting(t, doc_num, term_pos, p):
    p.setdefault(t, {})
    test = p[t]
    if len(test) < 3:
        test[doc_num] = [term_pos]
    else:
        try:
            test2 = test[doc_num]
            test2.append(term_pos)
            test[doc_num] = test2
        except KeyError:
            test[doc_num] = [term_pos]
    p[t] = test
    return p

def assemble_position_list():

    return

def search_term():
    term: str = input("Enter search term: ")
    while term.__contains__(" "):
        term: str = input("Please enter one term with no spaces: ")
    return term

def read_file_by_line():
    d = {}
    p = {}
    s_w_terms = use_stop_word()
    file: TextIO = open("cacm.all")
    extract_text = False
    doc_num = 0
    term_place = 0
    for x in file:
        if x[0:2] == ".W":
            extract_text = True
        elif x[0:2] == ".T":
            extract_text = True
        elif x[0:2] == ".A":
            extract_text = False
        elif x[0:2] == ".B":
            extract_text = False
        elif x[0:2] == ".I":
            term_place = 0
            doc_num = x.strip(x[0:3])
            doc_num = doc_num.strip("\n")
            extract_text = False
        elif x.strip('\n ') in (".X", ".C", ".K", ".N"):
            extract_text = False
        else:
            if extract_text:
                x = x.strip("\n")
                d, term_place, p = add_to_dictionary(x, d, s_w_terms, doc_num, term_place, p)
    file.close()
    return d, p

def use_stop_word():
    term: str = input("Use Stop Words enter yes: ")
    term = term.lower()
    if term == "yes" or term == "Yes":
        stop = open("stopwords.txt")
        stop_words = []
        for x in stop:
            stop_words.append(x.strip('\n'))
        stop.close()
        return stop_words
    return []



diction, posting_list_unorganized = read_file_by_line()
dictionary = list(diction.items())
dictionary.sort()
posting_list = list(posting_list_unorganized.items())
posting_list.sort()

pickle_out = open("dictionary.pickle", "wb")
pickle.dump(dictionary, pickle_out)
pickle_out.close()

pickle_out = open("posting.pickle", "wb")
pickle.dump(posting_list, pickle_out)
pickle_out.close()

#search: str = search_term()
#count: int = 0
#while search != "ZZEND":
#    count += 1
#    print(search)
#    search: str = search_term()
#print("Number of Times Search Ran: ", count)

