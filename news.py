import re
from bs4 import BeautifulSoup
import requests


print("\x1bc\x1b[43;30m")

page = requests.get("https://github.com/codebuil?tab=repositories")
s=BeautifulSoup(page.content,'html.parser')
ss=s.select_one("body")

ss=ss.select_one("main")
ss=ss.select("h3")
for n in list(ss):
    sss=n.select_one("a")
    print(sss.string.strip()+"->http://github.com"+sss.attrs.get("href"))




