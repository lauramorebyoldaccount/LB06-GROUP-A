import json
import urllib, urllib2

from textstat.textstat import textstat
from textblob import TextBlob
from keys import BING_API_KEY


if __name__ == '__main__':
    main()

def main():
    user_query = raw_input()
    run_query(user_query)
    
def run_query(search_terms):
    # Specify the base
    root_url = 'https://api.datamarket.azure.com/Bing/Search/'
    source = 'Web'

    # Specify how many results we wish to be returned per page.
    # Offset specifies where in the results list to start from.
    # With results_per_page = 10 and offset = 11, this would start from page 2.
    results_per_page = 10
    offset = 0

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)

    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''


    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, BING_API_KEY)

    # Create our results list which we'll populate.
    results = []

    try:
        # Prepare for connecting to Bing's servers.
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)

        # Loop through each page returned, populating out results list.
        for result in json_response['d']['results']:
            blob = TextBlob(result['Description'])
            for sentence in blob.sentences:
                sentiment_score = sentence.sentiment.polarity
                subjectivity_score = sentence.sentiment.subjectivity
                
            results.append({
            'title': result['Title'],
            'link': result['Url'],
            'summary': result['Description'],
            'flesch_score': '{0:.2f}'.format(textstat.flesch_reading_ease(result['Description'])),
            'sentiment_score': '{0:.2f}'.format(sentiment_score),
            'subjectivity_score': '{0:.2f}'.format(subjectivity_score),
            'source':'Bing'})


    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the Bing API: ", e

    # Return the list of results to the calling function.
    return results

