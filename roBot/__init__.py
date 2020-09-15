
from pyrogram import Client, filters
from pyrogram import __version__
import asyncio, json, sys
from time import time, sleep
from os import listdir
from rich.console import Console
konsol = Console()
def hata (yazi):
   konsol.print(yazi, style="bold red")
def bilgi (yazi):
   konsol.print(yazi, style="blue")
def basarili (yazi):
   konsol.print(yazi, style="bold green")
def onemli (yazi):
   konsol.print(yazi, style="bold cyan")
def soru (soru):
   return konsol.input(f"[bold yellow]{soru}[/]")
def anaLogo():
   surum = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}"
   konsol.print(f"\t\t\t[bold blue]@derleyiciBot[/] [yellow]:bird:[/]\t[bold red]Python: [/][i]{surum}[/]")
def baslangic():
   anaLogo()
   basarili(f"\t\tderleyiciBot v{__version__} pyrogram tabanında çalışıyor...\n")
bilgiler = json.load(open("bilgiler.json"))
derleyiciBot        = Client(
    api_id          = bilgiler['api_id'],                   # my.telegram.org/apps
    api_hash        = bilgiler['api_hash'],                 # my.telegram.org/apps
    session_name    = "@RunEverything_bot",                        # Fark Etmez
    bot_token       = bilgiler['bot_token'],                # @BotFather
    plugins         = dict(root="roBot/Eklentiler")
)
@derleyiciBot.on_message(filters.command(['start'], ['!','.','/']))
async def ilk(client, message):
    # Hoş Geldin Mesajı
    await message.reply_chat_action("typing")                           # yazıyor aksiyonu
    await message.reply("Hoş Geldin!\n/yardim alabilirsin.")            # cevapla
    # LOG Alanı
    sohbet = await derleyiciBot.get_chat(message.chat.id)
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if message.chat.type != 'private':
        log += f"\n\n\t\t`{sohbet.title}`__'den__ `{message.text}` __yolladı..__"
    else:
        log += f"\n\n\t\t`{message.text}` __yolladı..__"
    log +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
    await client.send_message(bilgiler['log_id'], log)                        # admin_id'ye log gönder
    #-------------------------------------------------------------------------#
@derleyiciBot.on_message(filters.command(['yardim'], ['!','.','/']))
async def yardim_mesaji(client, message):
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
    basla = time()
    await ilk_mesaj.edit("__Aranıyor...__")
    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id})!\n
Ben @ykslkrkci tarafından @santiyeyikodluyoruz için bir gece ansızın oluşturuldum.

.kazı Kullanımı : `.kazı` `|tabanboyu|` `|tabaneni|` `|kazıderinlik|` `|kazıeğimi|` \n
.istinat Kullanımı: `.istinat` `|duvarüstkalınlık|` `|duvaryükseklik|` `|temelarkagenislik|` `|temelöngenislik|` `|temeltoplamgenislik|` `|temelkalınlık|`\n
.mgm Kullanımı: `.mgm` `|Şehir|` \n
.döseme Kullanımı: `.mgm` `|uzunKenar|` `|kısaKenar|` `|kirisGenisliği|` `|uzundaÇalışan|` `|kısadaÇalışan|` \n
.maaliyet Kullanımı: `.maaliyet` `|Yıl|` `|yapıAlanı|` `|yapıGrubu|`\n
    """
    mesaj += "__Eklentilerim;__\n"

    for dosya in listdir("./roBot/Eklentiler/"):
        if not dosya.endswith(".py"):
            continue
        mesaj += f"📂 `{dosya.replace('.py','')}`\n"
    bitir = time()
    sure = bitir - basla
    mesaj += f"\n**Tepki Süresi :** `{str(sure)[:4]} sn`"
    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")

    # < LOG Alanı
    sohbet = await derleyiciBot.get_chat(message.chat.id)
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if message.chat.type != 'private':
        log += f"\n\n\t\t`{sohbet.title}`__'den__ `{message.text}` __yolladı..__"
    else:
        log += f"\n\n\t\t`{message.text}` __yolladı..__"
    log +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
    await client.send_message(bilgiler['log_id'], log)                        # admin_id'ye log gönder
    #-------------------------------------------------------------- Log Alanı >
@derleyiciBot.on_message(filters.command(['diller'],['!','.','/']))
async def giveLang(client,message):
    await message.reply_chat_action("upload_photo")
    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    #Foto Gönder
                       # Dosya Gönderiyor Aksiyonu
    foto = "roBot/dillerrr.png"
    await message.reply_photo(foto,reply_to_message_id = yanitlanacak_mesaj)
@derleyiciBot.on_message(filters.command(['eklenti'], ['!','.','/']))
async def eklenti_gonder(client, message):
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
    girilen_yazi = message.text                                 # komut ile birlikle mesajı tut
    if len(girilen_yazi.split()) == 1:                          # eğer sadece komut varsa
        await ilk_mesaj.edit("`DosyaAdı` **Girmelisin!**")      # uyarı ver
        return                                                  # geri dön
    dosya = " ".join(girilen_yazi.split()[1:2])                 # dosyayı komuttan ayır (birinci kelime)
    if f"{dosya}.py" in listdir("roBot/Eklentiler"):
        await ilk_mesaj.delete()
        if cevaplanan_mesaj is not None:
            await message.reply_document(
                document                = f"./roBot/Eklentiler/{dosya}.py",
                caption                 = f"__derleyiciBot__ `{dosya}` __eklentisi..__",
                disable_notification    = True,
                reply_to_message_id     = yanitlanacak_mesaj
                )
        else:
            await message.reply_document(
                document                = f"./roBot/Eklentiler/{dosya}.py",
                caption                 = f"__derleyiciBot__ `{dosya}` __eklentisi..__",
                disable_notification    = True,
                reply_to_message_id     = yanitlanacak_mesaj
                )
    else:
        await ilk_mesaj.edit('**Dosya Bulunamadı!**')
    # < LOG Alanı
    sohbet = await derleyiciBot.get_chat(message.chat.id)
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if message.chat.type != 'private':
        log += f"\n\n\t\t`{sohbet.title}`__'den__ `{message.text}` __yolladı..__"
    else:
        log += f"\n\n\t\t`{message.text}` __yolladı..__"
    log +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
    await client.send_message(bilgiler['log_id'], log)                        # admin_id'ye log gönder
    #-------------------------------------------------------------- Log Alanı >
