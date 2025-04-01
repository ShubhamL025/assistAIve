from flask import Blueprint, request, jsonify, session
import pymysql
import spacy
import nltk
from nltk.corpus import wordnet as wn
import enchant

chatbot_bp = Blueprint('chatbot', __name__)

nlp = spacy.load("en_core_web_sm")
english_dict = enchant.Dict("en_US")

def connect_to_database():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="admin",
        database="botdata",
        cursorclass=pymysql.cursors.Cursor
    )

def get_synonyms(word):
    synonyms = set()
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def preprocess_input(input_text):
    doc = nlp(input_text.lower())
    no_stop_words = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(no_stop_words)

def expand_synonyms(text):
    words = text.split()
    expanded_text = []
    for word in words:
        expanded_text.append(word)
        expanded_text.extend(get_synonyms(word))
    return ' '.join(expanded_text)

def correct_spelling(input_text):
    corrected_words = []
    for word in input_text.split():
        if english_dict.check(word):
            corrected_words.append(word)
        else:
            suggestions = english_dict.suggest(word)
            corrected_words.append(suggestions[0] if suggestions else word)
    return ' '.join(corrected_words)

@chatbot_bp.route("/chat", methods=["POST"])
def fetch_chatbot_info():
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        user_message = request.json.get("message")
        corrected = correct_spelling(user_message)
        preprocessed = preprocess_input(corrected)
        expanded = expand_synonyms(preprocessed)

        query = """
        SELECT name, url, description FROM ai_tools
        WHERE MATCH(name, description, keywords)
        AGAINST (%s IN NATURAL LANGUAGE MODE)
        LIMIT 1;
        """
        cursor.execute(query, (expanded,))
        result = cursor.fetchone()

        if result:
            name, url, description = result
            response = {
                "name": name,
                "url": f"<a href='{url}' target='_blank'>{url}</a>",
                "description": description
            }
        else:
            response = {
                "name": "Not Found",
                "url": "Not Found",
                "description": "Sorry, I couldn't find a matching AI tool for your query."
            }

        cursor.close()
        conn.close()
        return jsonify(response)

    except mysql.connector.Error as err:
        print("Database Error:", err)
        return jsonify({"error": "Internal server error."})
