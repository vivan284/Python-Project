import requests

r = requests.get("https://chatgpt.com/")
print(r.text)

with open("chatgpt.html", "w") as f:
    f.write(r.text)