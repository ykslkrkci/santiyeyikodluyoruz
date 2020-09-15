
import requests
from bs4 import BeautifulSoup as bs
from time import sleep

def kaziAlani(tavanAlani,tabanAlani,kaziDerinligi,kaziEgimi):
    base_link = "https://www.maliyetbul.com/lib.php?idx=11&A="+tavanAlani+"&B="+tabanAlani+"&H="+kaziDerinligi+"&D="+kaziEgimi

    r = requests.get(base_link).content
    soup = bs(r, "html.parser")
    return soup

