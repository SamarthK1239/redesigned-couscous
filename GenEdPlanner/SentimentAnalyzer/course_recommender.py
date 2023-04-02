import nltk
from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def recommender(lst_type):
    # Download the required NLTK resources
    nltk.download('punkt')
    nltk.download('stopwords')

    # Sample dataset: college course categories and descriptions
    course_categories = lst_type

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
    user_interest = "art, humanities, economic, psychology, speaking, philosophy, sex"

    # Process the user interest text and compute its similarity to the course category descriptions
    user_interest_bow = dictionary.doc2bow(preprocess_text(user_interest))
    user_interest_tfidf = tfidf[user_interest_bow]
    sims = index[user_interest_tfidf]

    # Sort course categories by similarity score and print the results
    sorted_sims = sorted(enumerate(sims), key=lambda x: x[1], reverse=True)
    counter = 0
    output = []
    for category_position, category_score in sorted_sims:
        #print(f"{course_categories[category_position]['title']} (score: {category_score:.2f})")
        output += [course_categories[category_position]['title']]
        counter += 1
        if counter == 3:
            break
    return output
