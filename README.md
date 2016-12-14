# Most Similar Tweets in Real-Time

### Description
The web application will allow users to type their tweets and be presented with a list of most similar tweets previously posted.
This is a feature that people can interact with and would like to use.

#### What This Repo Contains

- Presentation
- Model explained in detail
- Code

## Motivation

When we adopt a tool we also adopt the management philosophy embedded in that tool. Having the most similar tweets available to the author would significantly enhance the user experience on twitter by creating a strong sense of connection, encouraging creativity and expressivity, enriching communications and conversations and lead to much more exciting interactions on Twitter.
Trending Hashtags are consciously determined per tweet, usually offering creative variations or alternatives for the actual context of the tweet, sometimes even ironically unrelated phrases to express sarcasm; 
(hash)tags are secondary in importance as opposed to the tweet itself. Therefore, similarity of tweets is the more 
clear window into the flow of topics and use of language, and quickly result in growth of interaction.

## Challenge

The application has to process billions of tweets to find the most similar recommendations for any given new tweet as it is being typed. In order to implement this feature in real-time we must create a solution to significantly lower the computation run-time.

<div align="center"><img src="https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/Twinkle.png"></div>


## Real-Time solution

Sublinear scaling of runtime with sequential use of Hashing Vectorizer and Locality Sensitive Hashing Forest
- Similar items map to the same “buckets” with high probability (the number of buckets being much smaller than the universe of possible input items)
- LSHF generates hash trees
- Uses hashing to define a neighborhood
- Access to Nearest Neighbors Algorithm methods
- Search space is limited to a bucket
- Computes similarities to a small portion of tweets
- As the tweets grow, runtime stays the same

<div align="center"><img src=https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/Solution.png></div>


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

LSHForest uses internally random hyperplanes to index the samples into buckets and actual cosine similarities are only computed for samples that collide with the query hence achieving sublinear scaling.


<div align="center"><img src=https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/screenshot01.png></div>

<div align="center"><img src=https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/screenshot02.png></div>

#### Data

Twitter Streaming API

### Future Direction

Transformative Suggestions on tweets whilst editing the tweet - to be offered as a feature on Twitter.
"J.F.Kennedy: I would never lie to you." -> "I have integrity for greater good.”
This is modeled based on:
  * choice of words and expressions
  * context
  * intertextuality
  * measure of positivity
  * classification of sentiment
  * grammar and punctuation 
  * case-sensitivity
  * History of usage on Twitter
  * Conceptual vs literal alacrity and contradictions of the two:
Conceptual:  "John F. Kennedy: I would never lie to you." Literal: "Good Morning”
  * Giving weight-power to words: "Audacity of Hope" vs. "Make America Great Again”

#### References

* https://arxiv.org/pdf/1309.4168.pdf
* http://www.ncbi.nlm.nih.gov/pubmed/22250591
* https://cs224d.stanford.edu/reports/YuanYe.pdf
* http://karpathy.github.io/2015/05/21/rnn-effectiveness/
* https://dev.havenondemand.com/apis/analyzesentiment#overview
* https://papers.nips.cc/paper/5635-grammar-as-a-foreign-language.pdf
* https://www.researchgate.net/publication/221752656_The_Positivity_Scale
* http://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1010&context=leadershipfacpub


![alt tag](https://github.com/minoobeyzavi/Twinkle/blob/master/APP/static/img/Twitter.png)
