import requests as re
from bs4 import BeautifulSoup as be

url = 'https://www.intel.com/content/www/us/en/homepage.html'

res = re.get(url)

if res.status_code == 200:
    soup = be(res.content, 'html.parser')
    
    headers = soup.get_text()
    
    print(headers)
else:
    print(f'Failed to retrieve the web page. Status code: {res.status_code}')
