from flask import Flask, redirect, url_for, render_template, request, session
from services.interface import *

app = Flask(__name__)
app.secret_key = "8374tgrdsf8sdf973d4gf873gt36fgd7"

# ---------------------------------------------
# All books
# ---------------------------------------------
@app.route("/", methods=["GET"])
def main_page():
    if not session.get("title") is None:
        print(all_books())
        return render_template("index.html", books=all_books())
    return redirect(url_for("setto"))

# ---------------------------------------------
# Страница регистрации
# ---------------------------------------------
@app.route("/setting", methods=["GET"])
def setto():
    return render_template("books.html")

# ---------------------------------------------
# API's
# ---------------------------------------------
# ---------------------------------------------
# API регистрации
# ---------------------------------------------
@app.route("/api/v1/books", methods=["GET", "POST"])
def books_api():
    data = request.get_json()
    result_of_setting = setboo(data=data)
    print(result_of_setting)
    return json.dumps(result_of_setting)

if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT
    )