import os
import httpx
import openai

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

PROMPT_TEXT = """You are an experienced Magic: the Gathering player, and commander, or EDH, is your favorite format.
                 You love making unique, powerful, and fun commander decks for all your friends.
                 You will be given the name of legendary creature to be the commander of the deck, and sometimes some themes to base the deck around, and you will have to build a fully legal, 100 card commander deck.
                 Use whatever commander/EDH resources you need to research the deck.

                 Your only output should be a list of Magic: the Gathering card names separated by returns, like this:
                 |||
                 1 Elenda, the Dusk Rose
                 1 Sol Ring
                 1 Blood Artist
                 ...
                 |||

                 Be sure your deck has 100 cards."""

# credit to Eduardo Baccin for the skeleton of this method
def get_completion(content):
    try:
        print(f"Sending request for index: {index}")
        response = await httpx.post("https://api.openai.com/v1/chat/completions", headers=headers, json={
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": content}],
            "temperature": 1
        })

        response_json = response.json()
        completion_text = response_json["choices"][0]['message']["content"]

        return completion_text
    except Exception as e:
        print(f"Error at index {index}: {e}")
        return index, "Error"

def main:
    commander = input("Commander's Name: ")
    print("\n")
    themes = input("If you would like your deck to focus on any themes, write them here or write N/A:\n")
    prompt = PROMPT_TEXT + "\nCommander: " + commander + "\nThemes: " + themes
    response = get_completion(prompt, httpx)
    print(response)
    
