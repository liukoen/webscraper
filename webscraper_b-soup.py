import bs4
import requests
import re
regex_ex = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"

req = requests.get("http://www.sheldonbrown.com/web_sample1.html")
html_code=req.text
soup = bs4.BeautifulSoup(html_code, "html.parser")
url=[]
#print(soup.prettify())

links=soup.find_all(href=True)

#print(type(links))

for link in links:
    link_str=str(link)
    #print(link_str)
    if re.search(regex_ex,link_str):
        url.append(re.search(regex_ex,link_str).group(0))
     #   print(ma)
    #print(ur)
print(url)



