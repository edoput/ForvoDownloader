import requests


def Main(myfile, lang, apikey, limit):
      with open(myfile) as words:
            n=0
            while n < 250:
                  for i in words:
                  
                        #here some ceaning in wod format and something else
                        s = CorrectFormat(i)
                        
                        #let's make the request
                        r = ForvoHttpRequest('word-pronunciations',s,lang,apikey,limit)
                        
                        
                        #now we download the mp3 files from forvo server if r is "not-empty"
                        if r:
                              mp3 = requests.get(r)
                              file_path = i.replace('\n','')+'.mp3'
                              with open(file_path,"wb") as out:
                                    #we open a new mp3 file and we name it after the word we're downloading. The file it's opened in
                                    #write-binary mode
                                    out.write(mp3.content)
                        else:
                              if type(r)==None:
                                    with open('pending-pronounciation.txt','a') as out:
                                          out.write(s)
                              else:
                                    with open('pronuonce_not_found.txt','a') as out:
                                          out.write(s)
                        
                        n = n+1
def CorrectFormat(s):
      #here we prepare the string used, removing whitespace and escape character
      s = s.lower()                 #everithing to lower
      s = s.lstrip()                #remove head whitespace if any
      s = s.rstrip()                #remove tail whitespace if any
      s = s.replace(' ','%20')      #Forvo requires %20 to substitute whitespace in request's url
      s = s.replace('\n','')        #remove the escape character and does'nt replace it to prevent breaking the request's url
      return s
                  
        
def ForvoHttpRequest(act, word, lang, apikey, limit):
      #This is the url we need to use to send our request, it works when you use the 'word-pronunciations' action
      url = 'http://apifree.forvo.com/action/{0}/format/json/word/{1}/language/{2}/order/rate-desc/limit/{3}/key/{4}'.format(act, word, lang, limit, apikey)

      r = requests.get(url)
      #r is now  HTTP-request python object and we can use it's method, including reading server's json response
      data = r.json()
      
      if data:
            if data[u'items'][0][u'pathmp3']:         #Un dizionario in una lista in un dizionario
                  path = data[u'items'][0][u'pathmp3']
            else:
                  print "{0} isn't pronounced yet on Forvo.".format(word, lang)
                  path = None
      else:
            print "There isn't any JSON"
            path = ''
      return path
