import requests
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename

def Main(lang):
      #APIKEY is stored separately in another file called apikey
      with open('apikey.txt') as a:
        APIKEY=a.read()

      myfile = fileChoose()
      limit = input('How many pronounces for word?\n')
      
      with open(myfile) as words:
            #We will create a directory to store downloaded mp3, it will be named /home/user/forvo/...
            home        = os.path.expanduser('~/forvo')
            lang_dir    = os.path.join(home,lang)
            
            for i in words:
            
                  s = urllib.quote(i)
                  
                  r = ForvoHttpRequest('word-pronunciations',s,lang,APIKEY)

                  if r:
                        DownloadMp3(r, limit, i, lang_dir)
                  else:                        
                        file_name = os.path.join(lang_dir,'word_not_found.txt')
                        with open(file_name,'a') as out:
                              out.write(i)

                        
                                          
#TODO: remove CorrectFormat, replaced by urllib.quote()               
def CorrectFormat(s):
      #here we prepare the string used, removing whitespace and escape character
      
      s = s.lower()                 #everithing to lower
      s = s.lstrip()                #remove head whitespace if any
      s = s.rstrip()                #remove tail whitespace if any
      s = s.replace(' ','%20')      #Forvo requires %20 to substitute whitespace in request's url
      s = s.replace('\n','')        #remove the escape character and does'nt replace it to prevent breaking the request's url
      return s
                  
        
def ForvoHttpRequest(act, word, lang, apikey, path):
      #This is the url we need to use to send our request, it works when you use the 'word-pronunciations' action
      url = 'http://apifree.forvo.com/action/{0}/format/json/word/{1}/language/{2}/key/{3}'.format(act, word, lang, apikey)
      
      r = requests.get(url)
      #r is now HTTP-request python object and we can use it's method, including reading server's json response
      data = r.json()     
      
      if data[u'items']:
            #we retrieved a non empty JSON.
            #the JSON is structured like this:
            #a dictionary with 2 items, their keys are:
            #-u'attributes' (linked to info about the request we made)
            #-u'items' (linked to a list of dictionaries)
            #in the list there is a dictionary for every pronunciation, we will search for the "mp3path"
            
            paths = []
            for i in data[u'items']:
                  paths.append(i[u'pathmp3'])
            return paths
                  
      else:
            return None

def fileChoose():
      #show a file choose dialog box
      Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
      filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
      return filename

def DownloadMp3(urlList, limit, word, folder):
      #download a mp3 file, rename it and write it in a costum folder
      if urlList:
            for i in range(0,limit):
                  mp3 = requests.get(urlList[i])                 
                  
                  file_name   = word.replace('\n','')+'.{0}'.format(i)+'.mp3'
                  file_path   = os.path.join(folder, file_name)
                  
                  if not os.path.exists(folder):
                        os.makedirs(folder)              
                  else:
                        with open(file_path,"wb") as out:
                              #we open a new mp3 file and we name it after the word we're downloading.
                              #The file it's opened in write-binary mode
                              out.write(mp3.content)
      
