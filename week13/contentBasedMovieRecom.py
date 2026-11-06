from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = [
    "action superhero marvel fight",
    "dark superhero action detective",
    "superhero flying action hero",
    "romance ship love drama",
    "dream science fiction thriller"
]

names = ["Avengers", "Batman", "Superman", "Titanic", "Inception"]

# Convert descriptions into vectors
tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(movies)

# Calculate similarity
similarity = cosine_similarity(matrix)

# Select Batman
index = names.index("Batman")

# Sort similar movies
scores = list(enumerate(similarity[index]))
scores = sorted(scores, key=lambda x: x[1], reverse=True)

print("Recommended Movies for Batman:")

for i in scores[1:4]:
    print(names[i[0]])