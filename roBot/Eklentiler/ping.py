
from pyrogram import Client, filters
import asyncio
import datetime

@Client.on_message(filters.command(['ping'], ['!','.','/']))
async def ping(client, message):
    basla = datetime.datetime.now()
    
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

    mesaj = "__Pong!__"

    bitir = datetime.datetime.now()
    sure = (bitir - basla).microseconds/10000
    mesaj += f"\n\n**Tepki Süresi :** `{sure} ms`"

    await ilk_mesaj.edit(mesaj)
    
    await asyncio.sleep(3)
    await ilk_mesaj.edit("__Şantiyeyi Kodluyoruz__")
    await asyncio.sleep(1)
    await ilk_mesaj.edit(mesaj)