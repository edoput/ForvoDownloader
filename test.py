import forvo
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename

def Main(lang,limit):
      #APIKEY is stored separately in another file called apikey
      with open('apikey.txt') as a:
        APIKEY=a.read()

      myfile = fileChoose()
      
      with open(myfile) as words:
            #We will create a directory to store downloaded mp3, it will be named /home/user/forvo/...
            home        = os.path.expanduser('~/forvo')
            lang_dir    = os.path.join(home,lang)
            
            for i in words:
                  
                  r = ForvoRequest(i,lang,APIKEY)

                  if r:
                        DownloadMp3(r, limit, i, lang_dir)
                  else:                        
                        file_name = os.path.join(lang_dir,'word_not_found.txt')
                        with open(file_name,'a') as out:
                              out.write(i)

def fileChoose():
      #show a file choose dialog box
      Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
      filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
      return filename

def DownloadMp3(urlList, limit, word, folder):
      #download a mp3 file, rename it and write it in a costum folder
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
      
