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
                
                 Rules:
                 * Your deck must have exactly 100 cards and no card may appear more than once, except for basic lands
                 * Your deck must follow all color identity rules (ie a card cannot be included in the deck if it contains colors the commander does not).
                 * Be sure that each card name you include is a real Magic: the Gathering card that is legal in the Commander format
                 * Do not include any empty lines in your output
                 
                 Recommendations:
                 * Most commander decks run between 34 and 38 lands
                 * Almost all commander decks should dedicate multiple slots each to removal, ramp, card draw, and boardwipes
                 * If no theme is given, it is a good idea to pick a theme yourself based off the commander, and draw inspiration for other cards from that theme
                 
                 Steps:
                 1. Create the decklist for the given commander, with the themes given, if any, in the given output format.
                 2. Before sending your response, check each entry to make sure that all "Rules" are followed. If any rules are broken,
                 adjust the decklist as needed to make it match the rules (Ex. if a card appears more than once, replace the second occurence with different card that fulfills a similar role).
                 3. Output the list
                 """

# credit to Eduardo Baccin for the skeleton of this method
def get_completion(content):
    try:
        print(f"Sending request")
        response = httpx.post("https://api.openai.com/v1/chat/completions", headers=headers, json={
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": content}],
            "temperature": 1
        }, timeout=None)

        response_json = response.json()
        completion_text = response_json["choices"][0]['message']["content"]

        return completion_text
    except Exception as e:
        print(f"Error:" + str(e))
        return "Error"

def main():
    commander = input("Commander's Name: ")
    themes = input("If you would like your deck to focus on any themes, write them here or write N/A:\n")
    prompt = PROMPT_TEXT + "\nCommander: " + commander + "\nThemes: " + themes
    response = get_completion(prompt)
    print(response)

main()
    
