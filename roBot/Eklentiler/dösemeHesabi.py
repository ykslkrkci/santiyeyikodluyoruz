
from pyrogram import Client, filters
import asyncio

from roBot._İsciler import *

@Client.on_message(filters.command(['döseme'], ['!','.','/']))
async def derleyici(client, message):
    # < Başlangıç
    await message.reply_chat_action("typing")

    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    ilk_mesaj = await message.reply("__Hesaplanıyor..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    girilen_yazi = message.text
    
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Çalıştırabilmek için `uzunKenar` `kısaKenar` `kirisGenisliği` `uzundaÇalışan`  ve `kısadaÇalışan` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 2:
        await ilk_mesaj.edit("Çalıştırabilmek için `kısaKenar` `kirisGenisliği` `uzundaÇalışan`  ve `kısadaÇalışan` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 3:
        await ilk_mesaj.edit("Çalıştırabilmek için `kirisGenisliği` `uzundaÇalışan`  ve `kısadaÇalışan` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 4:
        await ilk_mesaj.edit("Çalıştırabilmek için `uzundaÇalışan`  ve `kısadaÇalışan` vermelisiniz..")
        return
    elif len(girilen_yazi.split()) == 5:
        await ilk_mesaj.edit("Çalıştırabilmek için `kısadaÇalışan` vermelisiniz..")
        return

    liste = girilen_yazi.split()
    print(liste)

    sonuc = Hesapla(int(liste[1]),int(liste[2]),int(liste[3]),int(liste[4]),int(liste[5]))
    
    if liste[4] == "2" and liste[5] == "0":
        print("2 uzun 0 kısa sürekli")
        görsel = "roBot\\dösemeGörsel\\a.jpg"
    elif liste[4] == "0" and liste[5] == "2":
        print("0 uzun 2 kısa sürekli")
        görsel = "roBot\\dösemeGörsel\\b.jpg"
    elif liste[4] == "1" and liste[5] == "1":
        print("1 uzun 1 kısa sürekli")
        görsel = "roBot\\dösemeGörsel\\c.jpg"
    elif liste[4] == "2" and liste[5] == "2":
        print("4 kenar sürekli")
        görsel = "roBot\\dösemeGörsel\\d.jpg"
    elif liste[4] == "2" and liste[5] == "1":
        print("2 uzun 1 kısa sürekli")
        görsel = "roBot\\dösemeGörsel\\e.jpg"
    elif liste[4] == "1" and liste[5] == "2":
        print("1 uzun 2 kısa sürekli")
        görsel = "roBot\\dösemeGörsel\\f.jpg"
    elif liste[4] == "1" and liste[5] == "0":
        print("1 uzun 2 kısa sürekli")
        görsel = "roBot\\dösemeGörsel\\g.jpg"
    elif liste[4] == "0" and liste[5] == "1":
        print("1 uzun 2 kısa sürekli")
        görsel = "roBot\\dösemeGörsel\\h.jpg"

    #görsel = "roBot\\istinat.png"
    mesaj = f"""Girilen Veriler:  Lu= `{liste[1]}cm`,  lk= `{liste[2]}cm`,  bw= `{liste[3]}cm`,  UzunC= `{liste[4]}`,  kısaC= `{liste[5]}`\n `Hesaplanan Döşeme Kalınlığı=` {round(sonuc,2)} cm"""
    await client.send_photo(
            message.chat.id,
            görsel,
            caption             =   mesaj,
            reply_to_message_id =   yanitlanacak_mesaj,
        )
    await ilk_mesaj.delete()
    