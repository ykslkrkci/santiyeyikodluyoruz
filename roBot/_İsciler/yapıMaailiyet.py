
import requests
from bs4 import BeautifulSoup as bs
from time import sleep

def Run(yil,alan,grup):
    base_link = "https://www.maliyetbul.com/lib.php?idx=50&M="+alan+"&Y="+yil+"&N="+grup

    r = requests.get(base_link).content
    soup = bs(r, "html.parser")
    return soup