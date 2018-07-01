import bs4
import requests
import re


req = requests.get("http://www.sheldonbrown.com/web_sample1.html")
html_code=req.text
soup = bs4.BeautifulSoup(html_code, "html.parser")

#print(soup.prettify())

links=soup.find_all(href=True)

#print(type(links))

for link in links:
    link_str=str(link)
    #print(link_str)
    if re.match("(www|http:|https:)+[^\s]+[\w]",link_str):
        print(link_str)

    #print(ur)




