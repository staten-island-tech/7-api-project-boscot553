import requests
import nltk
from nltk.corpus import words
import time

# Download the NLTK words list if not already installed
nltk.download('words')

# Function to get data from the dictionary API
def get_word_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()  # Parse the response as JSON
        print(f"Definitions for '{word}':")
        
        # Iterate through the results and print the meanings of the word
        for meaning in data[0]["meanings"]:
            part_of_speech = meaning["partOfSpeech"]
            print(f"Part of Speech: {part_of_speech}")
            for definition in meaning["definitions"]:
                print(f"Definition: {definition['definition']}")
                if "example" in definition:
                    print(f"Example: {definition['example']}")
                print("-" * 40)
    else:
        print(f"Error: Unable to fetch data for {word}")

# Fetch a list of words from NLTK
word_list = words.words()

# Iterate over each word and fetch its definition
for word in word_list:
    get_word_definition(word)
    
    # Add a delay to prevent hitting the API too quickly (optional)
  # Sleep for 1 second between requests to avoid rate limits