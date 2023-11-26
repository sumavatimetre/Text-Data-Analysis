#!/usr/bin/env python
# coding: utf-8

# # Text Data Analysis

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt


# In[2]:


comments = pd.read_csv(r'D:\DataSets\UScomments.csv',error_bad_lines=False)


# In[3]:


comments.head()


# In[4]:


comments.isnull().sum()


# In[5]:


comments.dropna(inplace=True)


# In[6]:


comments.isnull().sum()


# In[7]:


get_ipython().system('pip install textblob')


# In[8]:


from textblob import TextBlob


# In[9]:


comments.head()


# In[10]:


TextBlob("Logan Paul it's yo big day ‼️‼️‼️").sentiment.polarity


# In[11]:


sample_df =comments[0:1000]


# In[12]:


sample_df.shape


# In[13]:


polarity = []
for comment in comments["comment_text"]:
    try:
        polarity.append(TextBlob(comment).sentiment.polarity)
    except:
        polarity.append(0)
        


# In[14]:


len(polarity)


# In[15]:


comments['polarity']= polarity


# In[16]:


comments.head(5)


# In[17]:


filter1 = comments['polarity']==-1


# In[18]:


comments_negative = comments[filter1]


# In[19]:


filter2 = comments['polarity']==1
comment_positive = comments[filter2]


# In[20]:


comment_positive


# In[21]:


get_ipython().system('pip install Wordcloud')


# In[22]:


from wordcloud import WordCloud, STOPWORDS


# In[23]:


set(STOPWORDS)


# In[24]:


comments['comment_text']


# In[25]:


type((comments['comment_text']))


# In[26]:


total_comments_positive = ' '.join(comment_positive['comment_text'])


# In[27]:


total_comments_positive


# In[28]:


from wordcloud import WordCloud, STOPWORDS

# Assuming total_comments_positive is the text data you want to create a word cloud from
wordcloud = WordCloud(stopwords=set(STOPWORDS)).generate(total_comments_positive)


# In[29]:


import matplotlib.pyplot as plt

# Display the generated word cloud image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[30]:


total_comments_negative = ' '.join(comments_negative['comment_text'])


# In[31]:


wordcloud = WordCloud(stopwords=set(STOPWORDS)).generate(total_comments_negative)


# In[32]:


import matplotlib.pyplot as plt

# Display the generated word cloud image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[33]:


get_ipython().system('pip install emoji==2.2.o')



# In[34]:


import emoji


# In[35]:


emoji.__version__


# In[36]:


comments['comment_text'].head(6)


# In[37]:


comment =' trending 😉'


# In[38]:


[char for char in comment if char in emoji.EMOJI_DATA]


# In[39]:


''' emoji_list = []
for char in comment:
    if char in emoji.EMOJI_DATA:
        emoji_list.append(char)'''


# In[40]:


all_emoji_list = []
for comment in comments['comment_text'].dropna():
    for char in comment:
        if char in emoji.EMOJI_DATA:
            all_emoji_list.append(char)


# In[41]:


all_emoji_list[0:10]


# In[42]:


from collections import Counter


# In[43]:


Counter(all_emoji_list).most_common(10)


# In[44]:


freqs=[Counter(all_emoji_list).most_common(10)[i][1]for i in range(10)]


# In[45]:


freqs


# In[46]:


import plotly.graph_objs as go
from plotly.offline import iplot

# Assuming emoji_list is a list of emojis and freqs is a list of corresponding frequencies
emoji_list = ['😂', '😍', '❤', '🔥', '😭', '👏', '😘']
freqs = [36987, 33453, 31119, 8694, 8398, 5719, 5545]

trace = go.Bar(x=emoji_list, y=freqs)
layout = go.Layout(title='Emoji Frequencies', xaxis=dict(title='Emoji'), yaxis=dict(title='Frequency'))

fig = go.Figure(data=[trace], layout=layout)
iplot(fig)

