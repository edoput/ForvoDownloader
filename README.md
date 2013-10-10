ForvoDownloader
===============

<a href="http://www.forvo.com/" title="Pronunciations by Forvo"><img src="http://api.forvo.com/byforvoblue.gif" width="120" height="40" alt="Pronunciations by Forvo" style="border:0" /></a>

This is my first approach to the use of Forvo's API.

The whole project is now defined and ready.
Example
=======
This is not an executable file so you need to know at least a little Python to get thing up and running.
<strong>This script requires Requests to run. Get requests [here][3].</strong>

1. Get the [test.py][1] and [forvo.py][2] scripts.
2. Get an APIKEY from [Forvo][4]. You can sign for the free plan which allows you to make 500 requests per day.
Create a new file named apikey.txt and paste your APIKEY in it, save it and <b>place it in the same folder as the test.py script</b>.
3. Get a list of the words you want the script to check for on Forvo. It must be a plain-text file with one word per line.\*
4. The sintax to execute the script is:
``
    Main('Language'\*\*,limit)
``
5. Run the test.py script and choose your file from the dialog window.
6. Search the downloaded files in /user/forvo, there will be a different folder for each language.


\*Obviously you can put more than a word per line and it will search for the entire frase and whichever is the top rated will be downloaded, even if it's not the frase you're looking for.

\*\*Language must be a code from [this list](http://www.forvo.com/languages/alphabetically/). Example: 'English' -> 'en', 'French'  ->'fr'
To do
=====

- [ ] Wrap everything into a separate module
- [ ] Write a wiki

  [1]: /test.py   "test.py"
  [2]: /forvo.py  "forvo.py"
  [3]: http://docs.python-requests.org/en/latest/ "Requests latest"
  [4]: http://api.forvo.com "Forvo"
