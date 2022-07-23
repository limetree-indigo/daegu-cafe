from flask import Flask, render_template
from get_food_data import get_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data=get_data())


if __name__ == "__main__":
    app.run(debug=True)