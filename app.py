from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr
import string
import nltk
from nltk.corpus import stopwords

# Cargar el dataset
df = pd.read_csv('tedx_dataset.csv')

# Preprocesamiento de texto
nltk.download('stopwords')
stop_words = stopwords.words('english')

def remove_stopwords(text):
    imp_words = [word.lower() for word in str(text).split() if word.lower() not in stop_words]
    return " ".join(imp_words)

def clean_punctuations(text):
    punctuations_list = string.punctuation
    return text.translate(str.maketrans('', '', punctuations_list))

# Función para calcular similitudes
vectorizer = TfidfVectorizer(analyzer='word')
vectorizer.fit(df['details'])

def get_similarities(talk_content, data=df):
    talk_array1 = vectorizer.transform([talk_content]).toarray()
    sim = []
    pea = []
    for idx, row in data.iterrows():
        details = row['details']
        talk_array2 = vectorizer.transform([details]).toarray()

        cos_sim = cosine_similarity(talk_array1, talk_array2)[0][0]
        pea_sim = pearsonr(talk_array1.squeeze(), talk_array2.squeeze())[0]

        sim.append(cos_sim)
        pea.append(pea_sim)

    return sim, pea

def recommend_talks(talk_content, data=df):
    data['cos_sim'], data['pea_sim'] = get_similarities(talk_content)
    data = data.sort_values(by=['cos_sim', 'pea_sim'], ascending=[False, False])
    return data[['main_speaker', 'details']].head().to_dict(orient='records')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explanation')
def explanation():
    return render_template('explanation.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    talk_content = request.form['talk_content']
    recommendations = recommend_talks(talk_content)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
