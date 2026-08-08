import sys
import requests

def urls(out_file):
    url2 = sys.stdin.read().splitlines()
    good_url = []
    bad_url = []

    for url in url2:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                good_url.append(url)
        except requests.exceptions.MissingSchema:
            bad_url.append(url)
            continue
        except requests.exceptions.ConnectionError:
            bad_url.append(url)
            continue
    with open(out_file, 'w') as file:
        file.write('\n'.join(good_url))

    print(f"Saved URLS {out_file}")


out_file = 'filtered_urls.txt'
urls(out_file)

