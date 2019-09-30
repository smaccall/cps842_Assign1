import pickle
import time

def timerFinally(time):
    #print(time)
    avg = sum(time) / len(time)
    print('Average query search time ',avg)

def queryTerms():
    timer_list = []
    word_search = input('Word to query:')
    while word_search != 'ZZEND':
        start_timer = time.time()
        if word_search in dictObj :
            print('Document frequency :', dictObj[word_search])
            post_index = postObj[word_search]
            #For testing
            #print(postObj[word_search])
            for docID in post_index:
                freq_doc = post_index[docID][0]
                term_pos = str(post_index[docID][1]).lstrip('[').rstrip(']')
                print('Doc ID:',docID,'Frequency in doc ', freq_doc, ' in position(s)', term_pos )
        else:
            print("Not found")
        end_timer = time.time()
        print(end_timer - start_timer)
        timer_list.append(end_timer - start_timer)
        word_search = input('Word to query:')      
    print("End of search.")
    return timer_list

if __name__ == "__main__":
    # open the file for reading
    fileObject = open('dictionary.pickle','rb') 
    file2Object = open('posting.pickle','rb')  
    # load the object from the file
    dictObj = pickle.load(fileObject) 
    postObj = pickle.load(file2Object) 

    #For testing
    #print(dictObj)
    #print(postObj)
    time_log = queryTerms()
    timerFinally(time_log)
    

