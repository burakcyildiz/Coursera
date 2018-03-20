from pathlib import Path
import mailbox
import glob

def getbody(message): #getting plain text 'email body'
    body = None
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    elif message.get_content_type() == 'text/plain':
        body = message.get_payload(decode=True)
    return body


wordList = dict();
pathlist = glob.glob("/home/arkhenius/github/Coursera/Machine Learning/machine-learning-ex6/ex6/data/*/*")
# print(pathlist)
id = 1;
for path in pathlist:
    print("Progress:\t"+str(id)+" out of "+str(len(pathlist)))
    id += 1
    mbox = mailbox.mbox(path)
    for message in mbox:
        body = getbody(message)
        if body is not None:
            for word in body.split(): # iterate over each line
                if word.decode("ISO-8859-1") not in wordList:
                    wordList[word.decode("ISO-8859-1")] = 1
                else:
                    wordList[word.decode("ISO-8859-1")] += 1
#print(wordList)
index = 0
maxIndex = 3000
file = open("/home/arkhenius/github/Coursera/Machine Learning/machine-learning-ex6/ex6/data/vocabNew.txt","w")
for key in sorted(wordList, key=wordList.__getitem__, reverse=True):
    if index < maxIndex:
        file.write("{}\t{}\n".format(key, wordList[key]))
        index += 1
file.close()
