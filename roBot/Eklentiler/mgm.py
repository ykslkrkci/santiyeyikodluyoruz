

from pyrogram import Client, filters
import asyncio

from roBot._İsciler import *

@Client.on_message(filters.command(["mgm"],[".","!","/"]))
async def mgm(c,m):
    girilen_yazi = m.text
    if len(girilen_yazi.split()) == 1:
        await m.reply("`Arama yapabilmek için şehir belirtmelisiniz..`")
        return

    m_santiye =await  m.reply("`Hava Getiriliyor ..`")

    girdi = " ".join(girilen_yazi.split()[1:]).lower()

    try:
        cikti = hava(girdi)
        if cikti:
            await m_santiye.edit(cikti)
        else:
            await m_santiye.edit("`Herhangi bir veri bulamadım :))`")
    except Exception as hata:
        await m_santiye.edit("`Üzgünüm , birşeyler yanlış gitti .. {}`".format(str(hata)))

