##################################################################
from nltk.tag import pos_tag
import nltk
import string
import requests
import json


# def getMovieId(movieName, year):
#     url = "https://imdb8.p.rapidapi.com/title/find"

#     querystring = {"q": movieName}

#     headers = {
#         'x-rapidapi-host': "imdb8.p.rapidapi.com",
#         'x-rapidapi-key': "8d83ebf72cmshe58465d5ac91e85p13ec4cjsnc46687bd8d29"
#     }

#     response = requests.request(
#         "GET", url, headers=headers, params=querystring)
#     response_json = json.loads(response.text)
#     results_json = response_json['results']

#     for movie in results_json:
#         if (movie['year'] == year):
#             first_result_json = movie['id'][7:16]
#             movieIsInAPI = True
#             return first_result_json
#             break

# # Generate list of similar movies based on movie id


# def getSimilarMovies(movieId):
#     url = "https://imdb8.p.rapidapi.com/title/get-more-like-this"

#     querystring = {"currentCountry": "US",
#                    "purchaseCountry": "US", "tconst": movieId}

#     headers = {
#         'x-rapidapi-host': "imdb8.p.rapidapi.com",
#         'x-rapidapi-key': "8d83ebf72cmshe58465d5ac91e85p13ec4cjsnc46687bd8d29"
#     }

#     response = requests.request(
#         "GET", url, headers=headers, params=querystring)
#     response_json = json.loads(response.text)

#     movies = []
#     for movie in response_json:
#         movies.append(getDetails(movie[7:16]))

#     return movies


# def getDetails(movieId):
#     url = "https://imdb8.p.rapidapi.com/title/get-details"

#     querystring = {"tconst": movieId}

#     headers = {
#         'x-rapidapi-host': "imdb8.p.rapidapi.com",
#         'x-rapidapi-key': "8d83ebf72cmshe58465d5ac91e85p13ec4cjsnc46687bd8d29"
#     }

#     response = requests.request(
#         "GET", url, headers=headers, params=querystring)
#     response_json = json.loads(response.text)
#     movieTitle = response_json['title']
#     movieYear = response_json['year']
#     return (movieTitle, movieYear)

# ################################################################################


nltk.download('averaged_perceptron_tagger')

# Text Similarity Function


def textSimilarityAPI(input1, input2):
    url = "https://twinword-twinword-bundle-v1.p.rapidapi.com/text_similarity/"

    querystring = {"text1": input1, "text2": input2}
    headers = {
        'x-rapidapi-host': "twinword-twinword-bundle-v1.p.rapidapi.com",
        'x-rapidapi-key': "8d83ebf72cmshe58465d5ac91e85p13ec4cjsnc46687bd8d29"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    response_json = json.loads(response.text)
    return response_json['similarity']

# Lemmatizer to return roots of a string of words


def lemmatizerAPI(input):
    url = "https://twinword-twinword-bundle-v1.p.rapidapi.com/lemma_extract/"

    querystring = {"text": input}
    print(input)
    headers = {
        'x-rapidapi-host': "twinword-twinword-bundle-v1.p.rapidapi.com",
        'x-rapidapi-key': "8d83ebf72cmshe58465d5ac91e85p13ec4cjsnc46687bd8d29"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    response_json = json.loads(response.text)
    return response_json['lemma']

# Returns list of proper nouns


def findProperNouns(input, list2):
    sentence = input
    tagged_sent = pos_tag(sentence.split())
    fetchProperNouns = [word for word, pos in tagged_sent if pos == 'NNP']
    properNouns = []
    for item in fetchProperNouns:
        item = item.translate(str.maketrans('', '', string.punctuation))
        properNouns.append(item)
    for item in properNouns:
        if item in list2:
            properNouns.remove(item)
    return properNouns

# Word Association Function


def wordAssociationAPI(inputList):
    url = "https://twinword-twinword-bundle-v1.p.rapidapi.com/word_associations/"

    headers = {
        'x-rapidapi-host': "twinword-twinword-bundle-v1.p.rapidapi.com",
        'x-rapidapi-key': "8d83ebf72cmshe58465d5ac91e85p13ec4cjsnc46687bd8d29"
    }

    associatedWords = []

    for word in inputList:
        querystring = {"entry": word}
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        response_json = json.loads(response.text)
        associatedWords = associatedWords + response_json['associations_array']

    # remove duplicated words
    associatedWords = list(dict.fromkeys(associatedWords))
    print(len(associatedWords))
    return associatedWords

    # Sentiment Analysis Function

def sentimentAnalysisAPI(input1, input2):
    print(input1)
    print(input2)

    url = "https://twinword-twinword-bundle-v1.p.rapidapi.com/sentiment_analyze/"

    querystring = {"text": input1}

    headers = {
        'x-rapidapi-host': "twinword-twinword-bundle-v1.p.rapidapi.com",
        'x-rapidapi-key': "8d83ebf72cmshe58465d5ac91e85p13ec4cjsnc46687bd8d29"
    }

    input1Response = requests.request(
        "GET", url, headers=headers, params=querystring)
    input1Response = json.loads(input1Response.text)
    input1Sentiment = "positive" if input1Response['score'] > - \
        0.1 else "negative"

    querystring = {"text": input2}

    headers = {
        'x-rapidapi-host': "twinword-twinword-bundle-v1.p.rapidapi.com",
        'x-rapidapi-key': "8d83ebf72cmshe58465d5ac91e85p13ec4cjsnc46687bd8d29"
    }

    input2Response = requests.request(
        "GET", url, headers=headers, params=querystring)
    input2Response = json.loads(input2Response.text)
    input2Sentiment = "positive" if input2Response['score'] > - \
        0.1 else "negative"

    print("s1 : ", input1Sentiment)
    print("s2 : ", input2Sentiment)

    return input1Sentiment == input2Sentiment

# Compare Saved Event and Festival and return similarity index


def compareMovie(incomingMovieTitle, incomingMovieDescription, savedMovie):
    # Step 1: Get the similarity index using the Text Similarity API

    savedMovieDescription = savedMovie.synopsis

    savedMovieTitle = savedMovie.title
    
    textSIApi = textSimilarityAPI(savedMovieDescription, incomingMovieDescription)

    # Step 2

    savedMovieRootWords = lemmatizerAPI(savedMovieDescription)
    incomingMovieRootWords = lemmatizerAPI(incomingMovieDescription)

    # Check if both have the same root words and these common root words do
    # not include 'Singapore'

    # Step 3: For the title of the Movie, find the root words
    # and check whether root of T1 occur in T2
    # If common proper nouns do sentiment analysis


    # Step 3: Where the magic happens
    if (sentimentAnalysisAPI(savedMovieDescription, incomingMovieDescription)):
        savedMovieAssociatedWords = wordAssociationAPI(savedMovieRootWords)
        incomingMovieAssociatedWords = wordAssociationAPI(
            incomingMovieRootWords)

        commonalities = set(savedMovieAssociatedWords) - \
            (set(savedMovieAssociatedWords) - set(incomingMovieAssociatedWords))
        noCommonalities = len(commonalities)
        combinedAssociatedWords = savedMovieAssociatedWords + incomingMovieAssociatedWords
        noUniqueWords = len(combinedAssociatedWords) - noCommonalities
        siForAssociatedWords = noCommonalities / noUniqueWords

        textSIApi = textSIApi * (1 + siForAssociatedWords)

    return textSIApi

def compareEvent(incomingEventTitle, incomingEventDescription, savedEvent):
    # Step 1: Get the similarity index using the Text Similarity API

    savedEventDescription = savedEvent.description
    savedEventTitle = savedEvent.title

    # incomingEventTitle = getattr(incomingEvent, 'title')
    # incomingEventDescription = getatrr(incomingEvent, 'description')

    # savedEventDescription = getatrr(savedEvent, 'description')
    # savedEventTitle = getattr(savedEvent, 'title')
    
    textSIApi = textSimilarityAPI(savedEventDescription, incomingEventDescription)

    # Step 2

    savedEventRootWords = lemmatizerAPI(savedEventDescription)
    incomingEventRootWords = lemmatizerAPI(incomingEventDescription)

    savedEventProperNouns = findProperNouns(
        savedEventDescription, savedEventRootWords)
    incomingEventProperNouns = findProperNouns(
        incomingEventDescription, incomingEventRootWords)

    # Check if both have the same root words and these common root words do
    # not include 'Singapore'

    # Step 3: For the title of the event, find the root words
    # and check whether root of T1 occur in T2
    # If common proper nouns do sentiment analysis

    commonProperNouns = []

    for pNoun in savedEventProperNouns:
        if pNoun in incomingEventProperNouns and pNoun != 'Singapore':
            commonProperNouns.append(pNoun)

    # Step 3: Where the magic happens
    if (sentimentAnalysisAPI(savedEventDescription, incomingEventDescription)):
        if(len(commonProperNouns) > 0):
            noUniqueProperNouns = len(
                savedEventProperNouns + incomingEventProperNouns) - len(commonProperNouns)
            siForProperNouns = len(commonProperNouns) / noUniqueProperNouns
            textSIApi = textSIApi * (1 + siForProperNouns)

        savedEventAssociatedWords = wordAssociationAPI(savedEventRootWords)
        incomingEventAssociatedWords = wordAssociationAPI(
            incomingEventRootWords)

        commonalities = set(savedEventAssociatedWords) - \
            (set(savedEventAssociatedWords) - set(incomingEventAssociatedWords))
        noCommonalities = len(commonalities)
        combinedAssociatedWords = savedEventAssociatedWords + incomingEventAssociatedWords
        noUniqueWords = len(combinedAssociatedWords) - noCommonalities
        siForAssociatedWords = noCommonalities / noUniqueWords

        textSIApi = textSIApi * (1 + siForAssociatedWords)

    return textSIApi

def compareToSavedEvents(incomingEventTitle, incomingEventDescription, savedEventList):

    indexList = []

    for savedEvent in savedEventList:
        indexList.append(compareEvent(incomingEventTitle, incomingEventDescription, savedEvent))

    return max(indexList)

def compareToSavedMovies(incomingMovieTitle, incomingMovieDescription, savedMovieList):

    indexList = []

    for savedMovie in savedMovieList:
        indexList.append(compareMovie(incomingMovieTitle, incomingMovieDescription, savedMovie))

    return max(indexList)

# def recommendedMovieScore(incomingMovieTitle, incomingMovieYear, savedMoviesList):

#     shouldRecommend = False
#     movieId = getMovieId(incomingMovieTitle, incomingMovieYear)

#     simMovieIdList = getSimilarMovies(movieId)
    
#     for savedMovie in savedMoviesList:
#         savedMovieId = getMovieId(savedMovie.title, savedMovie.year)
#         if savedMovieId in simMovieIdList:
#             shouldRecommend = True
#             break
    
#     if shouldRecommend:
#         return 1
#     else:
#         return 0
