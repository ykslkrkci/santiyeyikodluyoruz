import requests
from bs4 import BeautifulSoup as bs
from time import sleep


def istinatDuvari(A,B,C,D,E,F):
    base_link = "https://www.maliyetbul.com/lib.php?idx=12&A="+A+"&B="+B+"&C="+C+"&D="+D+"&E="+E+"&F="+F
    r = requests.get(base_link).content
    soup = bs(r, "html.parser")
    return soup