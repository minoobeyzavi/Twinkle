# Most Similar Tweets in Real-Time
Display most similar tweets as a new tweet is being typed.
This is a feature that people can interact with and would like to use.

## Motivation

Today’s media is social which means that it consists not only of consumption but also expression and these two are
absolutely intertwined; whatever you consume has been expressed by someone else. Sharing your expression is the 
definition of caring what others think.
A social media personality is a performance. Those who can speak well, to the point and with lucidity, practice! 
Most people tend to experience and value a certain amount of reserve when it comes to expression on Twitter. 
That way they can preserve some of their mystery and subtlety. They can escape unnecessary judgment and recover the power 
of their own voice.
Having the recent similar tweets available to the author would significantly enhance the user experience on twitter by 
creating a perspective of how connected we are; encouraging creativity and expressivity, enriching communications and
conversations and lead to much more exciting interactions on Twitter.
Furthermore, trending and ignored hashtags are consciously determined per tweet, usually offering creative variations
or alternatives for the actual context of the tweet, sometimes even ironically unrelated phrases to express sarcasm; 
(hash)tags are secondary in importance as opposed to the tweet itself. Therefore, similarity of tweets is the more 
clear window into the flow of topics and use of language, and quickly result in growth of interaction. Twitter has 
already been training the society towards conciseness and inevitably thoughtfulness and proved that integrity in the 
architecture of a social media significantly increases its vitality.

![alt tag](https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/Twinkle.png)

## Description
The web application will allow users to type their tweets and be presented with a small list of most similar tweets previously posted.

## Real-Time solution

Filtered Tweets -> Hashing Vectorizer -> Locality Sensitive Hashing Forest

![alt tag](https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/Solution.png)

![alt tag](https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/screenshot01.png)

![alt tag](https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/screenshot02.png)

#### Data

Twitter Streaming API

#### What This Repo Contains

- Presentation
- Model explained in more detail.
- Code

### Future Direction

Transformative Suggestions on tweets whilst editing the tweet - to be offered as a feature on Twitter.
"J.F.Kennedy: I would never lie to you." -> "I have integrity for greater good”
This is modeled based on choice of words, context, strength of expressivity, expressions, grammar, punctuation, 
case-sensitivity, previous usage, conceptual vs literal alacrity and contradictions of the two
Conceptual:  "John F. Kennedy: I would never lie to you."
Literal: "Good Morning”
Giving weight power to words: "Audacity of Hope" vs. "Make America Great Again”

#### References

http://karpathy.github.io/2015/05/21/rnn-effectiveness/
https://dev.havenondemand.com/apis/analyzesentiment#overview
https://papers.nips.cc/paper/5635-grammar-as-a-foreign-language.pdf
https://www.researchgate.net/publication/221752656_The_Positivity_Scale
http://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1010&context=leadershipfacpub
