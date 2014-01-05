ForvoDownloader
===============

<a href="http://www.forvo.com/" title="Pronunciations by Forvo"><img src="http://api.forvo.com/byforvoblue.gif" width="120" height="40" alt="Pronunciations by Forvo" style="border:0" /></a>

This module can be used to retrieve a list of link to pronunciation to a a particular word from Forvo. This module require the [Requests module][3] to operate, install it from the python package index  before.

There is only a function to call and it requires 3 arguments, other are default values.

        ```
        import ForvoDownloader as forvo
        
        links = forvo.ForvoRequest(QUERY, LANG, apikey, ACT='word-pronunciations', FORMAT='mp3' free=TRUE)
        ```
* QUERY
* LANG
* apikey

are mandatory.

Please feel free to play around and implement other ACTIONS described in the [forvo API docs][4].

Language must be a code from [this list][5]. Example: 'English' -> 'en', 'French'  ->'fr'

Example
=======
This is not an executable file so you need to know at least a little Python to get thing up and running.
<strong>This script requires Requests to run. Get requests [here][3].</strong>

1. Get the [test.py][1] and [forvo.py][2] scripts.
2. Get an APIKEY from [Forvo][4]. You can sign for the free plan which allows you to make 500 requests per day.
Create a new file named apikey.txt and paste your APIKEY in it, save it and <b>place it in the same folder as the test.py script</b>.
3. Get a list of the words you want the script to check for on Forvo. It must be a plain-text file with one word per line.
4. The syntax to execute the test.py is: ```
            Main('Language',limit)
            ```
   You can find it on the bottom of the script.
5. Run the test.py script and choose your file from the dialog window.
6. Search the downloaded files in /user/forvo, there will be a different folder for each language.


Obviously you can put more than a word per line and it will search for the entire phrase and whichever is the top rated will be downloaded, even if it's not the phrase you're looking for.

To do
=====

- [x] Wrap everything into a separate module
- [ ] Write a wiki

  [1]: /test.py   "test.py"
  [2]: /forvo.py  "forvo.py"
  [3]: http://docs.python-requests.org/en/latest/ "Requests latest"
  [4]: http://api.forvo.com "Forvo API"
  [5]: http://www.forvo.com/languages/alphabetically/ "Forvo languages list"
