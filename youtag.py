import requests
from bs4 import BeautifulSoup
print("instert the url of youtube video:")
x= input()
if x[0:5] == "https":
    webpage_response = requests.get(x)
else:
    webpage_response = requests.get("https://"+x)
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
metatags = soup.find_all('meta',attrs={'name':'keywords'})
print(metatags)
