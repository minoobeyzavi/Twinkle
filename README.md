# Most Similar Tweets in Real-Time

Twinkle is a Natural Language Processing model capable of processing a growing database of billions of tweets and computing similarities in real-time, using a hashing vectorizer and a locality sensitive hashing forest sequentially to achieve sub-linear scaling of computation time.

This could be offered as a feature on Twitter, to view the most similar tweets simultaneously as the user is typing a new tweet.

#### What This Repo Contains

- Model Description
- Code
- Presentation
- Future Direction
- References

## Motivations

When we adopt a tool we also adopt the management philosophy embedded in that tool. Twitter is training social media users and the news audience across the planet towards conciseness and expressivity. Our continuous practice in use of language on social media is improving our integrity and refining our actions and personalities, swiftly leading to evolution of the society beyond traditional expectations. Twitter's presence strengthens the momentum towards living happier lives!

- **Growth of Positive Interactions** Having the most similar tweets available to the user would significantly enhance the user experience on twitter by creating a strong sense of connection, encouraging creativity and expressivity, enriching communication and lead to much more exciting interactions on Twitter. Hashtags usually offer creative variations or alternatives for the actual context of the tweet. Resemblence of the entire tweet however, displays a much more exciting connection and offering this feature would quickly increase positive interactions.
- **User Growth** Twitter is live: live commentary, live conversations, live connections; growth of positive interactions could be the most powerful opportunity to attract and increase the number of monthly active users and excite advertisers. Twitter is well-positioned to benefit from this headway.


 <!--<div align="center"><img src="https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/TwitterStats.png"></div>-->

## Challenge

The application has to process billions of tweets to find the most similar recommendations for tweets as they are being typed. In order to implement this feature in real-time we must create a solution to significantly lower the computation run-time!

<div align="center"><img src="https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/Twinkle.png"></div>


## Real-Time Solution

Sublinear scaling of runtime with <b>sequential use of Hashing Vectorizer and Locality Sensitive Hashing Forest</b>:
- Similar items map to the same “buckets” with high probability (the number of buckets are much smaller than the universe of possible inputs)
- LSH Forest generates hash trees
- Uses hashing to define a neighborhood
- Access to Nearest Neighbors algorithm methods
- Search space is limited to a bucket
- Finds the most similar tweets by computing similarities to a small portion of tweets

<b>As the database of text documents grows larger, runtime stays the same!</b>

<div align="center"><img src=https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/Solution.png></div>

## LSH Forest
<b>Locality Sensitive Hashing forest</b> is an alternative method for vanilla approximate nearest neighbor search methods. In Scikit-Learn, LSH forest data structure has been implemented using sorted arrays, binary search and 32 bit fixed-length hashes. Random projection is used as the hash family which approximates cosine distance.

```python
hv = HashingVectorizer(n_features=10000, non_negative=True)
docs_vectorized = hv.fit_transform(docs_joined).toarray()

# Local Sensitivity Hashing Forest
lshf = LSHForest(random_state=42, radius_cutoff_ratio=0.4)
lshf.fit(docs_vectorized)

# Hashing new input
new_doc_vectorized = hv.transform(new_doc).toarray()

# Distances & indices
dist, ind= lshf.radius_neighbors(new_doc_vectorized, return_distance=True)
```

LSHForest uses internally random hyperplanes to index the samples into buckets and cosine similarities are only computed for samples that collide with the query hence achieving sublinear scaling of computation time.


<div align="center"><img src=https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/screenshot01.png></div>

#### Data

- Twitter Streaming API
- The WordNet lemmatizer and word_tokenize functions from NLTK were applied to tokenize text documents prior to training the model.

## Future Direction

Offering <b>Transformative Suggestions</b> as a new tweet is being typed;
```
"JFK: I would never lie to you"  ->  "I have integrity for greater good”
```
This model is going to be designed based on:
  * <a href="https://en.wikipedia.org/wiki/Word-sense_induction">Word-Sense Induction</a>
  * Grammar
  * <a href="https://en.wikipedia.org/wiki/Intertextuality">Intertextuality</a>
  * Sentiment Analysis
  * Conceptual vs. Literal Alacrity</br>
```
  "Good Morning” => Literal
  "JFK: I would never lie to you." => Conceptual
```
  * Giving Weight-Power to Words:</br>
```
  "Audacity of Hope" vs. "Make America Great Again”
```

#### References

* https://arxiv.org/pdf/1309.4168.pdf
* http://www.nltk.org/book/ch08.html
* http://www.ncbi.nlm.nih.gov/pubmed/22250591
* https://cs224d.stanford.edu/reports/YuanYe.pdf
* http://karpathy.github.io/2015/05/21/rnn-effectiveness/
* http://alt.qcri.org/semeval2015/cdrom/pdf/SemEval002.pdf
* http://www.dubberly.com/articles/what-is-conversation.html
* https://dev.havenondemand.com/apis/analyzesentiment#overview
* https://papers.nips.cc/paper/5635-grammar-as-a-foreign-language.pdf
* http://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
* https://www.researchgate.net/publication/221752656_The_Positivity_Scale
* https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html
* http://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1010&context=leadershipfacpub

<div align="center"><img src=https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/Twitter.png></div>
