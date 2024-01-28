# Exploring LLMs' Capacity to Select Contextually Appropriate Suggestions for Conflict Resolution
## BTU Cottbus-Senftenberg. Conversational AI. WS 2023/2024.

This small project uses capability of [ChatGPT 4](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) to pick the most appropriate variant from the given ones based on the conversation. Focus is on facilitation conflict solving between individuals to make conversation as productive as possible.

### Running project:
1. Create .env file and add your `OPENAI_API_KEY`
2. Customize suggestion list in `suggestions.json` following the given format
3. Install dependencies and run Flask app `python app.py`
4. Insert dialog in the input field and press submit (see the demo in `/demo` folder)

**Note: dialog MUST be in a certain format, see `/example_dialogs` for examples!**

### Dependencies:

1. Install [pipenv](https://pipenv.pypa.io/en/latest/)
2. Activate virtual environment `pipenv shell`
