from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups 
from sklearn.metrics.pairwise import linear_kernel 
#twenty = fetch_20newsgroups()
twenty = ["hello there, I'm very happy","I'm feeling really good","everything is happy now","whatever happened here","go, go to the boom"]
tfidf = TfidfVectorizer().fit_transform(twenty) 
cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten() 
related_docs_indices = cosine_similarities.argsort()[:-3:-1] 
