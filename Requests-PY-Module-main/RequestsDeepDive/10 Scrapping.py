import requests
import os

links = [
    'https://www.codewithharry.com/blog',
    'https://www.codewithharry.com/contact',
    'https://www.codewithharry.com/tutorials'
]

os.makedirs("htmls", exist_ok=True)

for link in links:
    r = requests.get(link)

    page_name = link.rstrip('/').split('/')[-1]
    file_path = f"htmls/{page_name}.html"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(r.text)

    print(f"Saved {file_path}")
