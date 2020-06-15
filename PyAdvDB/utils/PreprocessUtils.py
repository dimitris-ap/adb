import dill
from nltk import re, tokenize, stem
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# PreProcess dependencies
stop_words = set(stopwords.words('english'))
w_tokenizer = tokenize.WhitespaceTokenizer()
lemmatizer = stem.WordNetLemmatizer()
vectorizer = TfidfVectorizer(max_features=10000, max_df=.8)


def clean_text(text):
    # remove backslash-apostrophe
    text = re.sub("\'", "", text)
    # remove everything except alphabets
    text = re.sub("[^a-zA-Z]", " ", text)
    # remove whitespaces
    text = ' '.join(text.split())
    # convert text to lowercase
    text = text.lower()
    return text


def remove_stopwords(text):
    no_stopword_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(no_stopword_text)


def lemmatize_text(text):
    lemmatized_text = [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)]
    return ' '.join(lemmatized_text)


def tf_idf(df):
    print('\nStarting Tf-Idf...')
    x = vectorizer.fit_transform(df.text.values).todense()

    print('Saving TF-IDF vectorizer to file...')
    export_tfidf_to_dill()
    print('Saved!')

    df['text'] = list(x)
    return df


def preprocess_single_query(tfidf_vectorizer, text):
    return tfidf_vectorizer.transform([lemmatize_text(remove_stopwords(clean_text(text)))])


def export_tfidf_to_dill():
    filename = 'vectorizer.dill'
    with open(filename, 'wb') as f:
        dill.dump(vectorizer, f)
