import bs4
import requests
import re
regex_ex = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
begin_url = input("Geef een URL op : ") or "http://www.sheldonbrown.com/web_sample1.html"
#print(soup.prettify())


def parse_link(urls_input):
    links=[]
    #print(urls_input)
    html_code=requests.get(urls_input).text
    soup = bs4.BeautifulSoup(html_code, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
    return links

l=parse_link(begin_url)

print(l)




