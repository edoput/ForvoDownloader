import requests

def Main(myfile, lang, apikey, limit):
      with open(apikey) as a:
        APIKEY=a.read()
        
      langUrl = 'http://apifree.forvo.com/key/{0}/format/json/action/language-list/order/name'.format(APIKEY)
      r = requests.get(langUrl)
      langList = r.json()
      
      with open(myfile) as words:
            for i in words:
                  print 'Searching {0}'.format(i)
            
                  #here some ceaning in word format and something else
                  s = CorrectFormat(i)
                  
                  #let's make the request
                  r = ForvoHttpRequest('word-pronunciations',s,lang,apikey)
                  
                  #now we download the mp3 files from forvo server if r is "not-empty"
                  if r:
                        print 'Downloading {0}'.format(i)
                        for i in range(0,limit):
                              mp3 = requests.get(r[i])
                              file_path = i.replace('\n','')+'.{0}'+'.mp3'
                              file_path.format(i)
                              
                              with open(file_path,"wb") as out:
                                    #we open a new mp3 file and we name it after the word we're downloading. The file it's opened in
                                    #write-binary mode
                                    out.write(mp3.content)
                                    
                  else:
                        with open('word_not_found.txt','a') as out:
                              out.write(i + '\n')                        
                        
def CorrectFormat(s):
      #here we prepare the string used, removing whitespace and escape character
      
      s = s.lower()                 #everithing to lower
      s = s.lstrip()                #remove head whitespace if any
      s = s.rstrip()                #remove tail whitespace if any
      s = s.replace(' ','%20')      #Forvo requires %20 to substitute whitespace in request's url
      s = s.replace('\n','')        #remove the escape character and does'nt replace it to prevent breaking the request's url
      return s
                  
        
def ForvoHttpRequest(act, word, lang, apikey):
      #This is the url we need to use to send our request, it works when you use the 'word-pronunciations' action
      url = 'http://apifree.forvo.com/action/{0}/format/json/word/{1}/language/{2}/key/{3}'.format(act, word, lang, apikey)
      
      r = requests.get(url)
      #r is now HTTP-request python object and we can use it's method, including reading server's json response
      data = r.json()     
      
      if data:
            #we retrieved a non empty JSON.
            #the JSON is structured like this:
            #a dictionary with 2 items, their keys are:
            #-u'attributes' (linked to info about the request we made)
            #-u'items' (linked to a list of dictionaries)
            #in the list there is a dictionary for every pronunciation, we will search for the "mp3path" key
            for i in data[u'items']:
                  #going throgt the list an appending mp3 link to paths
                  paths.append(i[u'pathmp3'])
                  return paths
                  
      else:
            #We retrieved an empty JSON beacuse there isn't any pronunciation
            return None

Main('parole_da_trovare.txt','da',APIKEY,1)
      
