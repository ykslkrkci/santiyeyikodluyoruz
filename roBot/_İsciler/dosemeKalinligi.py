import math as mt
def Hesapla(lu,lk,bw,uzun,kisa):
    llknet = lu - bw
    klknet = lk - bw
    m = lu / lk
    lsurekli = lu * uzun + lk + kisa
    toplam = (lu + lk) * 2
    a_s = lsurekli / toplam
    lsn = lk - bw
    isimsiz = (lsn)/(15 + (20/m))
    isimsiz2 = 1 - (a_s / 4)
    h = isimsiz * isimsiz2
    return h

    



    