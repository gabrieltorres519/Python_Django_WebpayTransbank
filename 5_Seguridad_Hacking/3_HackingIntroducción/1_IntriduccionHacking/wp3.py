import json
import urllib.request

# wp-json/wp/v2/users 
with urllib.request.urlopen('https://dazzet.co/wp-json/wp/v2/users') as response:
    html = response.read()
    for u in json.loads(html):
        print(u['slug'])