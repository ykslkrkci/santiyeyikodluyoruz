
from pyrogram import Client, filters
import asyncio

from roBot._İsciler import *

@Client.on_message(filters.command(['istinat'], ['!','.','/']))
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
        await ilk_mesaj.edit("Çalıştırabilmek için `üstduvargenislik` `duvaryüksekliği` `temelarkagenislik`  `temelöngenislik` ve `temelkalınlıgı` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 2:
        await ilk_mesaj.edit("Çalıştırabilmek için `duvaryüksekliği` `temelarkagenislik` `temelöngenislik` ve `temelkalınlıgı` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 3:
        await ilk_mesaj.edit("Çalıştırabilmek için `temelarkagenislik` `temelöngenislik` ve `temelkalınlıgı` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 4:
        await ilk_mesaj.edit("Çalıştırabilmek için `temelöngenislik` ve `temelkalınlıgı` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 5:
        await ilk_mesaj.edit("Çalıştırabilmek için `temelkalınlıgı` vermelisiniz..")
        return

    liste = girilen_yazi.split()

    hacim = istinatDuvari(liste[1],liste[2],liste[3],liste[4],liste[5],liste[6])
    
    görsel = "roBot\\istinat.png"
    mesaj = f"""Girilen Veriler: A=`{liste[1]}m`, B=`{liste[2]}m`, C=`{liste[3]}m`, D=`{liste[4]}m`, E=`{liste[5]}m`, F=`{liste[6]}m`\n `Toplam Beton Hacmi-Toplam Kazı Hacmi=` {hacim}m3"""
    await client.send_photo(
            message.chat.id,
            görsel,
            caption             =   mesaj,
            reply_to_message_id =   yanitlanacak_mesaj,
        )
    await ilk_mesaj.delete()

    #await ilk_mesaj.edit(f'`Toplam Beton Hacmi-Toplam Kazı Hacmi=` {hacim}m3')
    