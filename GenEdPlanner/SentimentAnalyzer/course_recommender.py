import nltk
from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample dataset: college course categories and descriptions
course_categories = [
    {
        'title': 'Arts',
        'description': 'Arts courses encourage creativity and self-expression, covering subjects such as painting, sculpture, photography, theater, and music.'
    },
    {
        'title': 'Mathematics',
        'description': 'Mathematics courses focus on the study of numbers, shapes, and patterns, covering topics like algebra, calculus, geometry, and statistics.'
    },
    {
        'title': 'Physics',
        'description': 'Physics courses explore the fundamental principles of the universe, covering topics such as mechanics, electricity, magnetism, thermodynamics, and quantum mechanics.'
    },
    {
        'title': 'Psychology',
        'description': 'Psychology courses delve into the study of human behavior and mental processes, exploring topics like cognition, emotion, motivation, and social interaction.'
    },
    {
        'title': 'Language',
        'description': 'Language courses focus on the development of communication skills, including reading, writing, speaking, and listening, in various languages such as English, Spanish, French, and Mandarin.'
    }
]

# Preprocess the text
stop_words = set(stopwords.words('english'))
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    return [token for token in tokens if token.isalnum() and token not in stop_words]

# Create a corpus from the course category descriptions
texts = [preprocess_text(category['description']) for category in course_categories]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Train a TF-IDF model
tfidf = models.TfidfModel(corpus)

# Compute similarities between course category descriptions using the trained model
index = similarities.MatrixSimilarity(tfidf[corpus])

# Example user interest text
user_interest = "I'm interested in studying human behavior and emotions."

# Process the user interest text and compute its similarity to the course category descriptions
user_interest_bow = dictionary.doc2bow(preprocess_text(user_interest))
user_interest_tfidf = tfidf[user_interest_bow]
sims = index[user_interest_tfidf]

# Sort course categories by similarity score and print the results
sorted_sims = sorted(enumerate(sims), key=lambda x: x[1], reverse=True)
for category_position, category_score in sorted_sims:
    print(f"{course_categories[category_position]['title']} (score: {category_score:.2f})")