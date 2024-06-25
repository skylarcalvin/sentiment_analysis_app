from flask import Flask, request, jsonify, render_template
from getSentiment import getSentiment as gs

# Initialize the Flask application.
app = Flask(__name__)

@app.route('/')
def index():
    '''
    Function renders the index template.
    '''
    return render_template('index.html')

# Direct the api call to the site root.
@app.route('/', methods = ['GET', 'POST'])
def parse_data():
    '''
    Function takes input from a web form and outputs sentiment.
    '''
    output = ''

    if request.method == 'POST':

        # Text from web form on the index template.
        text = request.form['text']

        sentiment_score = gs(text)

        output = f'The text you entered was {sentiment_score}.'

    return render_template('index.html', output = output)

if __name__ == '__main__':

    app.run()

