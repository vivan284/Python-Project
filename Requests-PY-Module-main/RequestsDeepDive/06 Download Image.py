import requests
from PIL import Image
from io import BytesIO
r = requests.get('https://media.gettyimages.com/id/2149530993/photo/digital-human-head-concept-for-ai-metaverse-and-facial-recognition-technology.jpg?s=612x612&w=0&k=20&c=IduORJUs1c1s0m2SXQANsK8IUhtlz8QApsLxNYOYrXQ=')
i = Image.open(BytesIO(r.content))
fp = open('image.jpg', 'wb')
i.save(fp)
fp.close()