from textblob import TextBlob

def emotion(text):
    # Analyze sentiment of the text
    analysis = TextBlob(text)
    
    # Determine sentiment
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"
