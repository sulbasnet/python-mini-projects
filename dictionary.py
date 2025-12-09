import requests

def meaning(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url).json()

        meanings = response[0]["meanings"][0]["definitions"][0]["definition"]
        example = response[0]["meanings"][0]["definitions"][0].get("example", "No example available.")

        print(f"\nWord: {word}")
        print(f"Meaning: {meanings}")
        print(f"Example: {example}")

    except:
        print("Word not found. Try another word.")

if __name__ == "__main__":
    print("=== Simple Dictionary App ===")
    word = input("Enter a word: ").lower()
    meaning(word)
