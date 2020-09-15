
from pyrogram import Client, filters
import asyncio

from roBot._İsciler import *

@Client.on_message(filters.command(['kazı'], ['!','.','/']))
async def derleyici(client, message):
    # < Başlangıç
    await message.reply_chat_action("typing")

    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    girilen_yazi = message.text
    
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Çalıştırabilmek için `tabanboyu` `tabaneni` `kazıderinliği` ve `kazıeğimi` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 2:
        await ilk_mesaj.edit("Çalıştırabilmek için `tabaneni` `kazıderinliği` ve `kazıeğimi` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 3:
        await ilk_mesaj.edit("Çalıştırabilmek için `kazıderinliği` ve `kazıeğimi` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 4:
        await ilk_mesaj.edit("Çalıştırabilmek için `kazıeğimi` vermelisiniz..")
        return

    liste = girilen_yazi.split()

    hacim = kaziAlani(liste[1],liste[2],liste[3],liste[4])
    görsel = "roBot\\kazı.png"
    mesaj = f"""Girilen Veriler:  A=`{liste[1]}m`,  B=`{liste[2]}m`,  H=`{liste[3]}m`,  D=`{liste[4]}°`\n`Toplam Kazı Hacmi=` {hacim}m3"""
    await client.send_photo(
            message.chat.id,
            görsel,
            caption             =   mesaj,
            reply_to_message_id =   yanitlanacak_mesaj,
        )
    await ilk_mesaj.delete()
    
    