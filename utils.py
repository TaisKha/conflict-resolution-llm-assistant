import os
import json
from openai import OpenAI

client = OpenAI()

def send_prompt(prompt: str) -> str:
  response = client.chat.completions.create(
    model="gpt-4-0125-preview",
    temperature=0.1,
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": prompt},
    ]
  )
  data = response.choices[0].message.content
  
  return data

  

def summarize_chat(messages=[("Alice", "Hi"), ("Bob", "Hi Alice, how are you?")]):

  messages_text = "\n".join([f"{name}: {text}" for name, text in messages])
  prompt = "This is the conversation. Please, summarize the conversation.\n\n" + messages_text + "\n\nSummary:"
  
  return send_prompt(prompt)

def get_suggestions_list() -> list[str]:
  with open("suggestions.json", "r") as file:
    content = json.load(file)
    suggestions = [str(suggestion["id"]) + ". " + str(suggestion["text"]) for suggestion in content["suggestions"]]

  return suggestions

def choose_from_suggestions(messages, suggestions: list[str]) -> str:
  messages_text = "\n".join([f"{name}: {text}" for name, text in messages])
  prompt = "This is the conversation:\n\n" + messages_text + "\n\nPlease, choose from the following suggestions what would be the most appropriate to consider next:\
      \n\n" + "\n".join(suggestions) + "\n\n Chosen suggestion:"
  
  print(prompt)
  return send_prompt(prompt)

def choose_from_suggestions_using_summary(conversation_summary: str, suggestions: list[str]) -> str:
  prompt = "This is the summary of the conversation:\n\n" + conversation_summary + "\n\nPlease,\
      choose from the following suggestions what would be the most appropriate to consider next:\
      \n\n" + "\n".join(suggestions) + "\n\n Chosen suggestion:"
  
  print(prompt)
  return send_prompt(prompt)

def parse_dialog(dialogue_human_readable: str) -> list[tuple[str, str]]:
  # Split the dialogue into individual lines
  dialogue_lines = dialogue_human_readable.split('\n')

  # Parse each line to extract speaker and dialogue
  dialogue_tuples = []
  for line in dialogue_lines:
      speaker, dialogue = line.split(': ', 1)
      dialogue_tuples.append((speaker, dialogue))

  return dialogue_tuples    

def get_suggestion_from_original_dialog(dialogue_human_readable: str) -> str:
  # Parse the dialogue into a list of tuples
  dialogue_tuples = parse_dialog(dialogue_human_readable)

  # Get suggestions
  suggestions = get_suggestions_list()

  # Choose the best suggestion
  suggestion = choose_from_suggestions(dialogue_tuples, suggestions)

  return suggestion

# Alternative version of the function get_suggestion_from_original_dialog
def get_suggestion_using_summary(dialogue_human_readable: str) -> str:
  # Parse the dialogue into a list of tuples
  dialogue_tuples = parse_dialog(dialogue_human_readable)

  # Summarize the dialogue
  dialogue_summary = summarize_chat(dialogue_tuples)

  # Get suggestions
  suggestions = get_suggestions_list()

  # Choose the best suggestion
  suggestion = choose_from_suggestions_using_summary(dialogue_summary, suggestions)

  return suggestion
  

#   messages_set_2 = [("Emily", "John, we need to pivot our business strategy."),
#     ("John", "That's too risky, Emily. Our current approach is solid."),]
#   messages_set_1 = [("Alice", "Bob, you never do your share of the chores!"),
#     ("Bob", "I do plenty around here! You're just being stupid and unreasonable."),
#     ("Alice", "Lol, you're always calling me stupid. Can't you think of a better insult?"),
# ]
#   messages_set_3 = [("Sarah", "David, your objections are stalling progress on the project!"),
#     ("David", "I have valid concerns, Sarah. We need to address them.")]
  



  


""