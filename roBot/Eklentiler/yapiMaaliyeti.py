from pyrogram import Client, filters
import asyncio
from roBot._İsciler import *
@Client.on_message(filters.command(['maaliyet'], ['!','.','/']))
async def derleyici(client, message):
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
        await ilk_mesaj.edit("Çalıştırabilmek için `Yıl` , `yapıAlanı` ve `yapıGrubu` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 2:
        await ilk_mesaj.edit("Çalıştırabilmek için `yapıAlanı` ve `yapıGrubu` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 3:
        await ilk_mesaj.edit("Çalıştırabilmek için `yapıGrubu` vermelisiniz..")
        return
    liste = girilen_yazi.split()
    dosya = "roBot\\maaliyet.pdf"
    await ilk_mesaj.reply_document(dosya)
    sonuc = Run(liste[1],liste[2],liste[3])
    #görsel = "roBot\\kazı.png"
    mesaj = f"""Girilen Veriler:  Yıl=`{liste[1]}`,  Alan=`{liste[2]}m2`,  Grup=`{liste[3]}``\n`Çıktı=` {sonuc}tl"""
    #await client.send_photo(
    #        message.chat.id,
    #        görsel,
    #        caption             =   mesaj,
    #        reply_to_message_id =   yanitlanacak_mesaj,
    #    )
    #await ilk_mesaj.delete()
    await ilk_mesaj.edit(mesaj)
    
    