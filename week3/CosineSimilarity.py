from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#example sentences
s1 = "data science is fun"
s2 ="science makes data useful"

#convert text tovextor representation
vectorizer = CountVectorizer().fit([s1, s2])
vectors = vectorizer.transform([s1, s2])

#compute cosine similarity
cos_sim = cosine_similarity(vectors[0],vectors[1])[0][0]
print("Cosine  similarity:",cos_sim)