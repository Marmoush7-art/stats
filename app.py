from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Le 'use_reloader=False' évite les bugs sur Spyder/Windows
    app.run(debug=True, use_reloader=False)