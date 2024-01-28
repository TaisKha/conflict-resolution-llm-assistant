from flask import Flask, render_template, request
from utils import get_suggestions_list

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    suggestions = get_suggestions_list()
    if request.method == 'POST':
        user_input = request.form['user_input']

        # Process user input and interact with ChatGPT (to be implemented)
        response = "Response from LLM: " + user_input
        return render_template('index.html', suggestions=suggestions, response=response)

    return render_template('index.html', suggestions=suggestions, response=None)

if __name__ == '__main__':
    app.run(debug=True)