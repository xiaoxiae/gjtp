import urllib.request
import httplib2
from re import match, MULTILINE
from bs4 import BeautifulSoup

http = httplib2.Http()
status, response = http.request("https://www.gymnaziumjihlava.cz/")

soup = BeautifulSoup(response, features="lxml")
input_tag = soup.find_all(attrs={"class" : "mb-md-0"})

print(str(input_tag[0])[19:-4])
