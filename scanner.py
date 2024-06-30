import requests
from bs4 import BeautifulSoup as bsf
import inquirer
import pyfiglet
from yaspin import yaspin
import time

result = pyfiglet.figlet_format("URL Scanner", font="slant")
print(result)
one = True


while one:
    unit = inquirer.list_input("To do:", choices=['scan'])
    url = input("Enter URL: ")
    res = requests.get(url)
    soup = bsf(res.text, 'html.parser')
    with yaspin().white.bold.shark.on_blue as sp:
        sp.text="Fetching Links....."
        time.sleep(5)
    for link in soup.find_all('a'):
        print(link.get('href'))
    unit = input("Do you want to scan another url: (y/n) ").lower()
    if unit == 'n':
        print("exiting.....")
        one = False