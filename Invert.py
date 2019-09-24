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
                    post_list = add_to_posting(term, doc_num, term_pos, post_list)
                    term_pos += 1
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
        test[doc_num] = [1, [term_pos]]
    else:
        try:
            test2 = test[doc_num]
            test3 = test2[1]
            test3.append(term_pos)
            test2[1] = test3
            freq = test2[0]
            test2[0] = freq + 1
            test[doc_num] = test2
        except KeyError:
            test[doc_num] = [1, [term_pos]]
    p[t] = test
    print (p)
    return p

def assemble_position_list():

    return

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

def pickle_file(x, p):
    pickle_out = open(x, "wb")
    pickle.dump(p, pickle_out)
    pickle_out.close()

if __name__ == "__main__":
    diction, posting_list_unorganized = read_file_by_line()
    dictionary = list(diction.items())
    dictionary.sort()
    posting_list = list(posting_list_unorganized.items())
    posting_list.sort()
    pickle_file("dictionary.pickle", dictionary)
    pickle_file("posting.pickle", posting_list)
