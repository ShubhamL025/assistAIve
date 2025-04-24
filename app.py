from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import mysql.connector
from datetime import datetime
import spacy
import nltk
from nltk.corpus import wordnet as wn
import enchant
import re

app = Flask(_name_)
app.secret_key = 'your_secret_key_here'

nlp = spacy.load("en_core_web_sm")
english_dict = enchant.Dict("en_US")
nltk.download('wordnet')
nltk.download('omw-1.4')

def correct_spelling(text):
    corrected = []
    for word in text.split():
        if english_dict.check(word):
            corrected.append(word)
        else:
            suggestions = english_dict.suggest(word)
            corrected.append(suggestions[0] if suggestions else word)
    return ' '.join(corrected)

def get_synonyms(word):
    synonyms = set()
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
    return synonyms

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return tokens

def expand_keywords(tokens):
    expanded = set(tokens)
    for token in tokens:
        expanded |= get_synonyms(token)
    return list(expanded)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ROY@2405",
        database="assistaive"
    )

def fetch_all_tools():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ai_tools")
    tools = cursor.fetchall()
    cursor.close()
    conn.close()
    return tools

def fetch_top_tools(user_input, top_n=3):
    corrected = correct_spelling(user_input)
    tokens = clean_text(corrected)
    expanded = expand_keywords(tokens)
    tools = fetch_all_tools()
    scores = []
    for tool in tools:
        content = f"{tool.get('keywords', '')} {tool.get('description', '')}".lower()
        content_tokens = clean_text(content)
        match_score = sum(token in content_tokens for token in expanded)
        if match_score > 0:
            scores.append((tool, match_score))
    scores.sort(key=lambda x: x[1], reverse=True)
    top_results = [tool for tool, _ in scores[:top_n]]
    if len(top_results) < top_n:
        doc_input = nlp(user_input.lower())
        sim_scores = []
        for tool in tools:
            desc = tool.get("description", "")
            doc_tool = nlp(desc.lower())
            sim = doc_input.similarity(doc_tool)
            sim_scores.append((tool, sim))
        sim_scores.sort(key=lambda x: x[1], reverse=True)
        for tool, sim in sim_scores:
            if tool not in top_results and sim > 0.5:
                top_results.append(tool)
                if len(top_results) == top_n:
                    break
    return top_results

def save_chat(user_id, user_msg, bot_response):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (user_id, user_message, bot_response) VALUES (%s, %s, %s)", (user_id, user_msg, bot_response))
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def root():
    return redirect(url_for('register'))

@app.route('/chat')
def chat():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM chat_history WHERE user_id = %s", (user_id,))
    total_chats = cursor.fetchone()[0]
    cursor.execute("SELECT username, email, role FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('index.html', username=user_data[0], email=user_data[1], role=user_data[2], chat_count=total_chats)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json["prompt"]
    user_id = session.get('user_id')
    greetings = ["hi", "hello", "hey", "yo", "hola"]
    if user_input.strip().lower() in greetings:
        response = "Hey there! 👋 I'm assistAIve. How can I help you explore the world of AI today?"
        save_chat(user_id, user_input, response)
        return jsonify([{"name": "assistAIve", "description": response, "url": ""}])
    tools = fetch_top_tools(user_input)
    response = "Here are some tools I found for you!" if tools else "Sorry, I couldn't find any tools matching that."
    save_chat(user_id, user_input, response)
    return jsonify(tools if tools else [{"name": "assistAIve", "description": response, "url": ""}])

@app.route('/get_history')
def get_history():
    user_id = session.get('user_id')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT user_message, bot_response, timestamp FROM chat_history WHERE user_id = %s", (user_id,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/admin/activities')
def view_all_activities():
    if session.get('role') != 'admin':
        return "Unauthorized", 403
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT u.username AS username, u.email AS email, c.user_message AS message,
               c.bot_response AS response, c.timestamp AS timestamp
        FROM chat_history c
        JOIN users u ON c.user_id = u.id
        ORDER BY c.timestamp DESC
    """)
    chats = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("admin_activities.html", chats=chats)

@app.route('/admin/feedback')
def view_feedback():
    if session.get('role') != 'admin':
        return "Unauthorized", 403
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT f.id,
               COALESCE(u.username, 'Anonymous') AS name,
               f.user_email,
               f.message,
               f.submitted_at
        FROM feedback f
        LEFT JOIN users u ON f.user_email = u.email
        ORDER BY f.submitted_at DESC
    """)
    feedback_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("admin_feedback.html", feedbacks=feedback_data)

@app.route('/get_feedback')
def get_feedback():
    if session.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT f.id,
               COALESCE(u.username, 'Anonymous') AS name,
               f.user_email,
               f.message,
               f.submitted_at
        FROM feedback f
        LEFT JOIN users u ON f.user_email = u.email
        ORDER BY f.submitted_at DESC
    """)
    feedback_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(feedback_data)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    feedback = data.get('feedback')
    user_email = session.get("user_email")
    username = session.get("username")
    if feedback:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO feedback (username, user_email, message) VALUES (%s, %s, %s)", (username, user_email, feedback))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'status': 'success'})
        except Exception as e:
            print("MySQL Error:", e)
            return jsonify({'status': 'error', 'message': 'DB insert failed'}), 500
    return jsonify({'status': 'error', 'message': 'Feedback was empty'}), 400

@app.route('/clear_history', methods=['POST'])
def clear_history():
    user_id = session.get('user_id')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chat_history WHERE user_id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/surprise')
def surprise():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ai_tools ORDER BY RAND() LIMIT 1")
    tool = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(tool)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username, email, password = request.form['username'], request.form['email'], request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            flash("Username already exists!")
            return redirect(url_for('register'))
        cursor.execute("INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)", (username, email, password, "user"))
        session['username'], session['user_id'], session['user_email'] = username, cursor.lastrowid, email
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('chat'))
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'], session['user_id'], session['role'], session['user_email'] = username, user[0], user[4], user[2]
            return redirect(url_for('chat'))
        flash("Invalid credentials")
        return redirect(url_for('login'))
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out!")
    return redirect(url_for('login'))

@app.route('/get_user_role')
def get_user_role():
    return jsonify({'role': session.get('role', 'user')})

if _name_ == '_main_':
    app.run(debug=True)
