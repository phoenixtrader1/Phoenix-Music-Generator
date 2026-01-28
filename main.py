from flask import Flask, render_template, request
from ai.music import generate_music
from users.wallet import get_balance
from utils.token import use_token

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    username = request.args.get("user", "user1")
    message = ""
    output = None

    if request.method == "POST":
        prompt = request.form.get("prompt")
        success, msg = use_token(username)
        message = msg

        if success:
            output = generate_music(prompt)

    balance = get_balance(username)
    return render_template(
        "dashboard.html",
        username=username,
        message=message,
        output=output,
        balance=balance
    )
