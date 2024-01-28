from flask import Flask, render_template, request
from utils import get_suggestions_list, get_suggestion_from_original_dialog

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    suggestions = get_suggestions_list()
    if request.method == 'POST':
        user_input = request.form['user_input']

        # If user input does not contain ":", then set response to ""
        if ":" not in user_input or len(user_input) == 0:
            response = ""
        else:
            response = get_suggestion_from_original_dialog(user_input)
        return render_template('index.html', suggestions=suggestions, response=response)

    return render_template('index.html', suggestions=suggestions, response=None)

if __name__ == '__main__':
    app.run(debug=True)