from flask import Blueprint, render_template, request, redirect, session
import mysql.connector

auth_bp = Blueprint('auth', __name__)

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="botdata"
    )

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                           (username, email, password))
            conn.commit()
            return redirect("/login")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            cursor.close()
            conn.close()

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect("/")
        else:
            return "Login failed. Incorrect email or password."

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
