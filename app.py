from flask import Flask, render_template, session, redirect
from auth.routes import auth_bp
from chatbot.chatbot import chatbot_bp
import webbrowser
import threading

app = Flask(__name__)
app.secret_key = 'abc123'

app.register_blueprint(auth_bp)
app.register_blueprint(chatbot_bp)

@app.route('/')
def home():
    if 'username' not in session:
        return redirect('/login')
    return render_template("index.html", username=session.get("username"))

def open_browser():
    webbrowser.open("http://127.0.0.1:5000/login")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(debug=True)
