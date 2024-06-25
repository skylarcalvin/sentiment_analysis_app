from nltk.sentiment.vader import SentimentIntensityAnalyzer

def getSentiment(payload):
    '''
    Function assigns sentiment to each document in the corpus and adds them as a new row on the dataframe.
    '''

    # Build sentiment analyzer.
    analyzer = SentimentIntensityAnalyzer()
    sentiment = [analyzer.polarity_scores(payload)]
    print(sentiment)
    # Label the rows using the compound sentiment score.
    if sentiment[0]['compound'] > 0.05:
        
        if sentiment[0]['compound'] > 0.5:
            
            value = 'very positive'
            
        else:
            
            value = 'positive'
        
    elif sentiment[0]['compound'] < -0.05:
        
        if sentiment[0]['compound'] < -0.5:
            
            value = 'very negative'
            
        else:
            
            value = 'negative'
        
    else:
        
        value = 'neutral'
    
    return value
