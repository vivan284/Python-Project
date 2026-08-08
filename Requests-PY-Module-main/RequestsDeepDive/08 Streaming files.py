import requests
from tqdm import tqdm

url = 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-713.exe'

r = requests.get(url, stream=True)
total_size = int(r.headers.get('content-length', 0))

progress = tqdm(total=total_size, unit='B', unit_scale=True)

with open('winrar.exe', 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:  # avoid empty chunks
            f.write(chunk)
            progress.update(len(chunk))

progress.close()
