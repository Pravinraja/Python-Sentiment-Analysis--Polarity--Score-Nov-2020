#!/usr/bin/env python
# coding: utf-8

# In[3]:


from textblob import TextBlob
text = '''
Mark is a bad guy. Who stole over 500k worth of cars and was a huge reason of election fraud in Arizona. He is evil 
and should not be trusted. 
'''
tb=TextBlob(text)
print(tb.sentiment.polarity)


# In[2]:


from textblob import TextBlob
from mediawiki import MediaWiki
wikipedia = MediaWiki()

text = wikipedia.page('Pizza')
content= text.content

tb=TextBlob(content)
print(tb.sentiment.polarity)
#food, it about half at 45. because pizza tastes good, but it also is unhealthy and can cause many health issues


# In[1]:


from textblob import TextBlob
from mediawiki import MediaWiki
wikipedia = MediaWiki()

text = wikipedia.page('Bitchute')
content= text.content

tb=TextBlob(content)
print(tb.sentiment.polarity)
# very negative because this a far right website that promotes radical views. many sources say that it
#"hosts "hate-fueled material"


# In[6]:


from textblob import TextBlob
text = '''
Andrew was a great person and teamplayer. He never cared about winning and only played for the fun of the game.
He is a good role model, however he does semll bad and needs to take more showers..
'''
tb=TextBlob(text)
print(tb.sentiment.polarity)


# In[11]:


from textblob import TextBlob
from mediawiki import MediaWiki
wikipedia = MediaWiki()

text = wikipedia.page('Sad')
content= text.content

tb=TextBlob(content)
print(tb.sentiment.polarity)
#low score because this is obvious


# In[14]:


from textblob import TextBlob
from mediawiki import MediaWiki
wikipedia = MediaWiki()

text = wikipedia.page('LehmanBrothers')
content= text.content

tb=TextBlob(content)
print(tb.sentiment.polarity)
#average score. because the company collapsed: "too big to fail", but was also a major company in the 20th century
#in the banking sector


# In[15]:


from textblob import TextBlob
from mediawiki import MediaWiki
wikipedia = MediaWiki()

text = wikipedia.page('Super Size Me')
content= text.content

tb=TextBlob(content)
print(tb.sentiment.polarity)

#low score because this documentary by spurlock uses a lot of words that attack the fast food indusry
#and the reviews section was controversial on how these 30 tests were done. 


# In[ ]:




