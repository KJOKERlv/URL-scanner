import requests
from bs4 import BeautifulSoup as bsf
import inquirer
import pyfiglet
from yaspin import yaspin
import time

result = pyfiglet.figlet_format("URL Scanner", font="slant")
print(result)
print("          CREATOR: Kjokerlv ")
print("    email: kjokerhamcs@gmail.com ")
print("   github: https://github.com/KJOKERlv ")
one = True


while one:
    print("choose operation")
    print("[1] Scan Url links")
    print("[2] Exit")
    choice = input(">> ")
    if choice == '1':
        
       url = input("Enter URL: ")
       res = requests.get(url)
       soup = bsf(res.text, 'html.parser')
       with yaspin().white.bold.shark.on_blue as sp:
         sp.text="Fetching Links....."
         time.sleep(5)
       for link in soup.find_all('a'):
         print(link.get('href'))
    elif choice == '2':
        print("exiting........")
        one = False
