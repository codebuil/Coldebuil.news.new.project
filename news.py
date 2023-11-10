import re
from bs4 import BeautifulSoup
import requests



page = requests.get("https://github.com/codebuil?tab=repositories")
s=BeautifulSoup(page.content,'html.parser')
ss=s.select_one("h3.wb-break-all")
sss=ss.select_one("a")

print("\x1bc\x1b[43;30m")

print("codebuil site news code:")
print(sss.string)

