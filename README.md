# autocomplete
This is a HTTP web service in Flask restplus that provides an endpoint for fuzzy search or autocomplete feature for English Words.
The endpoint is described below:

GET /search?word=&lt;input&gt;

where input is the (partial) word that the user has typed so far and that input is searched in a dataser that contains 333,333 English words and the frequency of their usage in some corpus.

For example, if the user is looking up procrastination, the service might receive this sequence of requests:

GET /search?word=pro

GET /search?word=procr

GET /search?word=procra

and so on.

The service is returning a response of JSON array containing upto 25 results, ranked by some criteria (see
below).

Constraints:
------------
1. Matches can occur anywhere in the string, not just at the beginning. For example, eryx should match archaeopteryx (among others).

2. The ranking of results should satisfy the following:

  a. We assume that the user is typing the beginning of the word. Thus, matches at the start of a word should be ranked higher. For example, for the input pract, the result 
     practical should be ranked higher than impractical.
  b. Common words (those with a higher usage count) should rank higher than rare words.
  c. Short words should rank higher than long words. For example, given the input environ, the result environment should rank higher than environmentalism.
     Note: As a corollary to the above, an exact match should always be ranked as the first result.
     
RUNNING THE FLASK APPLICATION:
---------------------------------
1. Install Flask-Restplus using pip : pip install flask-restplus

2. Install Flask : pip install Flask

3. Install Flask-Cors : pip install Flask-Cors

4. Installing and running Flask App : 
    Go to project directory and run the below commands to run the application on local host (Windows):
    
    set FLASK_APP=autocomplete.py
    
    flask run
    
    Change &lt;set&gt; to &lt;export&gt; in order to run the project on linux. 
    
    After running the commands please check the URL : http://localhost:5000/index to check the UI.
    
    Please Note : 
    -------------
    http://localhost:5000/ , this URL will take you to the Swagger UI as Swagger comes by-default with Flask Restplus framework. 
     
