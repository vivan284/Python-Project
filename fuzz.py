import requests
import sys

def fuzz():
    for word in sys.stdin:
        word = word.strip()
        if not word:
            continue

        try:
            res = requests.get(url=f"http://localhost:5000/{word}")
            
            # Skip 404s and keep going
            if res.status_code == 404:
                continue

            # Print matching results
            print(f"[{res.status_code}] /{word}")
            try:
                print(res.json())
            except ValueError:
                print(res.text[:100])  # Print raw text snippet if response isn't JSON

        except requests.exceptions.RequestException as e:
            print(f"Error connecting for '{word}': {e}")

if __name__ == "__main__":
    fuzz()
