import requests as re
from bs4 import BeautifulSoup as be

url = "https://www.intel.com/content/www/us/en/homepage.html"

res = re.get(url)
if res.status_code == 200:
    so = be(res.text,"html.parser")
    txt = so.get_text()
    lin = [a['href'] for a in so.find_all('a',href = True)]
    img = [i['src'] for i in so.find_all('i',src = True)]

    print("\nTEXT CONTENT\n")
    print(txt)
    print("\nLINKS\n")
    for link in lin:
        print(link)
    print("\nIMAGES\n")
    for image in img:
        print(image)

else:
    print(f'Failed to retrieve the web page. Status code: {res.status_code}')