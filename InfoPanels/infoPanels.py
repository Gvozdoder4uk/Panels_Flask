from flask import Flask, render_template
import random

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return render_template('info_panels.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")