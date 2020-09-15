from pyrogram import Client,filters
import requests as r
from bs4 import BeautifulSoup as bs
from datetime import datetime

def hava(girdi):
    girdi = girdi.replace("ş", "s")
    girdi = girdi.replace("ç", "c")
    girdi = girdi.replace("ı", "i")
    girdi = girdi.replace("ö", "o")
    girdi = girdi.replace("ü", "u")
    girdi = girdi.replace("ğ", "g")

    link = "https://www.havadurumu15gunluk.net/havadurumu/"+girdi+"-hava-durumu-15-gunluk.html"
    ham = r.get(link)
    if ham.status_code != 200:
        return "`200 dönmeyen kod ! {}`".format(ham.status_code)
    html = ham.text
    soup = bs(html, "html.parser")
    Sicaklık = soup.find("strong", {"class": "strong2"}).text
    Durum = soup.find("strong", {"class": "strong3"}).text

    mesaj = ""
    Il = girdi.capitalize()
    an = datetime.now()
    mesaj += f"`Son Güncelleme: {datetime.strftime(an,'%X')}`\n"
    mesaj += "__İl__ -".rjust(20)+"`{}`\n".format(Il)
    mesaj += "__Sıcaklık__ -".rjust(20)+"`{}`\n".format(Sicaklık)
    mesaj += "__Durum__ -".rjust(20)+"`{}`\n\n".format(Durum)
    if Durum == "-":
        return ""
    else:
        return mesaj
