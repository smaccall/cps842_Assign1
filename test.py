import pickle
import time

def timerFinally(time):
    #print(time)
    avg = sum(time) / len(time)
    print('Average query search time ',avg)

def extraInfo(x,y,wordObj):
    if x in wordObj:
        #print(wordObj[x][0])
        #print(wordObj[x][1])
        if y in [item.lower() for item in wordObj[x][0]]:
            pos = [item.lower() for item in wordObj[x][0]].index(y)
            if len(wordObj[x][0]) <=11:
                print(" ".join(wordObj[x][0]))
            else: 
                if pos-5 < 0:
                    left = abs(pos-5)
                    summary = wordObj[x][0][0:pos+1]
                    summary.extend(wordObj[x][0][pos+1:pos+left+6])
                    print(" ".join(summary))
                elif pos+5 > len(wordObj[x][0]):
                    left = (len(wordObj[x][0])+1)-pos
                    summary = wordObj[x][0][pos-5-left:pos] + wordObj[x][0][pos:len(wordObj[x][0])+1]
                    print(" ".join(summary))
                else:
                    print(" ".join(wordObj[x][0][pos-5:pos+6]))
        else:
            pos = [item.lower() for item in wordObj[x][1]].index(y)
            if len(wordObj[x][1]) <=11:
                print(" ".join(wordObj[x][1]))
            else:
                if pos-5 < 0:
                    left = abs(pos-5)
                    summary = wordObj[x][1][0:pos+1]
                    summary.extend(wordObj[x][1][pos+1:pos+left+6])
                    print(" ".join(summary))
                elif pos+5 > len(wordObj[x][1]):
                    left = (len(wordObj[x][1])+1)-pos
                    summary = wordObj[x][1][pos-5-left:pos] + wordObj[x][1][pos:len(wordObj[x][1])+1]
                    print(" ".join(summary))
                else:
                    print(" ".join(wordObj[x][1][pos-5:pos+6]))
                
def queryTerms(dictObj,postObj,wordObj):
    timer_list = []
    word_search = input('Word to query:')
    while word_search != 'ZZEND':
        word_search = word_search.lower()
        start_timer = time.time()
        if word_search in dictObj :
            print('Document frequency :', dictObj[word_search])
            post_index = postObj[word_search]
            #For testing
            #print(postObj[word_search])
            for docID in post_index:
                freq_doc = post_index[docID][0]
                term_pos = str(post_index[docID][1]).lstrip('[').rstrip(']')
                print('Doc ID:',docID, '. Title:', " ".join(wordObj[docID][0]), '. Frequency in doc ', freq_doc, ' in position(s)', term_pos )
                extraInfo(docID,word_search,wordObj)
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
    file3Object = open('document_words.pickle','rb')
    # load the object from the file
    dictObj = pickle.load(fileObject) 
    postObj = pickle.load(file2Object) 
    wordObj = pickle.load(file3Object)
    #For testing
    #print(dictObj)
    #print(postObj)
    #print(wordObj)
    time_log = queryTerms(dictObj,postObj,wordObj)
    timerFinally(time_log)
    

