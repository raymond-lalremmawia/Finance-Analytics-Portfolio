import requests
from bs4 import BeautifulSoup

# Getting the URL using request library, and assigning a variable to it
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
print(r)
print(r.text)

# lxml to print the html codes
# text to print it as text version
Soup = BeautifulSoup(r.text,"lxml")
print(Soup.div.ul)

# To print the attributes under the division tags
tag = Soup.div
print(tag.attrs)

# To print the attributes under the header tags
tag = Soup.header
print(tag.attrs)

# To print the items under class or role
tag = Soup.header
atb = (tag.attrs)
print(atb["class"])
print(atb["role"])

# To print without the tags, you can insert "string" either as "Soup.div.p.string" or "print(tag.string)"
tag = Soup.div.p
print(tag.string)

# Else, it will be printed with the tags here
tag = Soup.header.div.a.button.span
print(tag)

tag = Soup.header.div.a.button.span
print(tag.string)

# Use the find() function to extract the data needed from a div class
# Inspect the div class you want and copy the html code like below
# Print the data you need. Print it as string to remove the unnessary HTML text
price = (Soup.find("h4",{"class":"float-end price card-title pull-right"}))
print(price.string)

Desc = (Soup.find("p",{"class":"description card-text"}))
print(Desc.string)

# The limitation of the find() function is that it only extracts the data from the first div class of a web page
# The find_all() function is used to replace this weakness
Desc = (Soup.find_all_next("p",{"class":"description card-text"}))
print(Desc.string)