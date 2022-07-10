# Python-Sentiment-Analysis-Nov-2020

As we get the wiki articles we want to calculate sentiment of each one. One easy NLP library is TextBlob. TextBlob contains a basic polarity method rating articles from -1 to 1. Here is a basic example of how to use it

#pip install TextBlob
from textblob import TextBlob
tb=TextBlob(text)
print(tb.sentiment.polarity)



For the Assignment Calculate the Overall Polarity for at least 5 different pages on wikipedia. Try to find them in different genres (politics, history, science, celebrity, etc) Report on their totals. 

 

Try to construct your own very positive sentences and your own very negative sentences (try 2-3 of each). Report how it does. 
