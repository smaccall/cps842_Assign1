from typing import TextIO

def search_term():
    term: str = input("Enter search term: ")
    while term.__contains__(" "):
        term: str = input("Please enter one term with no spaces: ")
    return term

def read_file_by_line():
    file: TextIO = open("cacm.all")
    line_needed = False
    new_doc = False
    doc_num = ""
    extract = False
    for x in file:
        if x[0:2] == ".W":
            extract = True
            line_needed = True
        elif x[0:2] == ".T":
            extract = True
            line_needed = True
        elif x[0:2] == ".A":
            line_needed = True
            extract = False
        elif x[0:2] == ".B":
            line_needed = True
            extract = False
        elif x[0:2] == ".I":
            new_doc = True
            doc_num = x.strip(x[0:3])
        elif x.strip('\n ') in (".X", ".C", ".K", ".N"):
            line_needed = False
            extract = False
        else:
            if extract:
                print(x)
        if new_doc:
            new_doc = False
            print(doc_num)
    file.close()

def use_stop_word():
    stop = open("stopwords.txt")
    stop_words = []
    for x in stop:
        stop_words.append(x.strip('\n'))
    stop.close()
    return stop_words

#s_w_terms = use_stop_word()

read_file_by_line()

#search: str = search_term()
#count: int = 0
#while search != "ZZEND":
#    count += 1
#    print(search)
#    search: str = search_term()
#print("Number of Times Search Ran: ", count)

