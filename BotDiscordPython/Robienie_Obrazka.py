from PIL import Image, ImageFont, ImageDraw
import sqlite3


def obrazek():
    conn = sqlite3.connect("mapy.db")
    c = conn.cursor()

    img = Image.open(r'staty.png')
    font = ImageFont.truetype("arial.ttf", 30)
    font2 = ImageFont.truetype("arial.ttf", 20)

    c.execute("SELECT nazwa FROM mapy")
    z = c.fetchall()
    c.execute("SELECT liczba FROM mapy")
    a = c.fetchall()
    c.execute("SELECT win FROM mapy")
    v = c.fetchall()
    c.execute("SELECT lose FROM mapy")
    b = c.fetchall()
    c.execute("SELECT draw FROM mapy")
    n = c.fetchall()
    c.execute("SELECT win_lose FROM mapy")
    m = c.fetchall()

    mapy = []
    liczby = []
    winy = []
    lose = []
    drawy = []
    winy_lose = []
    for mapa in z:
        x = str(mapa).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        mapy.append(x)
    for liczba in a:
        x = str(liczba).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        liczby.append(x)
    for win in v:
        x = str(win).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        winy.append(x)
    for losey in b:
        x = str(losey).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        lose.append(x)
    for drawey in n:
        x = str(drawey).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        drawy.append(x)
    for winyilosy in m:
        x = str(winyilosy).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        winy_lose.append(x)

    w, h = font.getsize(str(mapy[:1]))
    draw = ImageDraw.Draw(img)
    draw.text(((200 - w) / 2, (70 - h) / 2), "Nazwa mapy", font=font, fill="white")
    draw.text(((200 - w) / 2, (200 - h) / 2), str(mapy[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (270 - h) / 2), str(mapy[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (340 - h) / 2), str(mapy[2]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (410 - h) / 2), str(mapy[3]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (480 - h) / 2), str(mapy[4]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (550 - h) / 2), str(mapy[5]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (620 - h) / 2), str(mapy[6]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (690 - h) / 2), str(mapy[7]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (760 - h) / 2), str(mapy[8]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (830 - h) / 2), str(mapy[9]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (900 - h) / 2), str(mapy[10]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (970 - h) / 2), str(mapy[11]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (1050 - h) / 2), str(mapy[12]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (1130 - h) / 2), str(mapy[13]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((650 - w) / 2, (75 - h) / 2), "Liczba gier", font=font, fill="white")
    draw.text(((780 - w) / 2, (200 - h) / 2), str(liczby[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (270 - h) / 2), str(liczby[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (340 - h) / 2), str(liczby[2]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (410 - h) / 2), str(liczby[3]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (480 - h) / 2), str(liczby[4]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (550 - h) / 2), str(liczby[5]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (620 - h) / 2), str(liczby[6]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (690 - h) / 2), str(liczby[7]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (760 - h) / 2), str(liczby[8]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (830 - h) / 2), str(liczby[9]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (900 - h) / 2), str(liczby[10]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (970 - h) / 2), str(liczby[11]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (1050 - h) / 2), str(liczby[12]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (1130 - h) / 2), str(liczby[13]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((1050 - w) / 2, (75 - h) / 2), "Wygrane", font=font, fill="white")
    draw.text(((1160 - w) / 2, (200 - h) / 2), str(winy[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (270 - h) / 2), str(winy[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (340 - h) / 2), str(winy[2]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (410 - h) / 2), str(winy[3]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (480 - h) / 2), str(winy[4]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (550 - h) / 2), str(winy[5]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (620 - h) / 2), str(winy[6]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (690 - h) / 2), str(winy[7]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (760 - h) / 2), str(winy[8]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (830 - h) / 2), str(winy[9]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (900 - h) / 2), str(winy[10]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (970 - h) / 2), str(winy[11]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (1050 - h) / 2), str(winy[12]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (1130 - h) / 2), str(winy[13]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((1400 - w) / 2, (75 - h) / 2), "Przegrane", font=font, fill="white")
    draw.text(((1510 - w) / 2, (200 - h) / 2), str(lose[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (270 - h) / 2), str(lose[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (340 - h) / 2), str(lose[2]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (410 - h) / 2), str(lose[3]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (480 - h) / 2), str(lose[4]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (550 - h) / 2), str(lose[5]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (620 - h) / 2), str(lose[6]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (690 - h) / 2), str(lose[7]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (760 - h) / 2), str(lose[8]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (830 - h) / 2), str(lose[9]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (900 - h) / 2), str(lose[10]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (970 - h) / 2), str(lose[11]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (1050 - h) / 2), str(lose[12]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (1130 - h) / 2), str(lose[13]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((1800 - w) / 2, (75 - h) / 2), "Remisy", font=font, fill="white")
    draw.text(((1900 - w) / 2, (200 - h) / 2), str(drawy[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (270 - h) / 2), str(drawy[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (340 - h) / 2), str(drawy[2]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (410 - h) / 2), str(drawy[3]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (480 - h) / 2), str(drawy[4]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (550 - h) / 2), str(drawy[5]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (620 - h) / 2), str(drawy[6]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (690 - h) / 2), str(drawy[7]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (760 - h) / 2), str(drawy[8]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (830 - h) / 2), str(drawy[9]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (900 - h) / 2), str(drawy[10]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (970 - h) / 2), str(drawy[11]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (1050 - h) / 2), str(drawy[12]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (1130 - h) / 2), str(drawy[13]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((2150 - w) / 2, (75 - h) / 2), "Win/Lose", font=font, fill="white")
    draw.text(((2240 - w) / 2, (200 - h) / 2),
              str(winy_lose[0]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (270 - h) / 2),
              str(winy_lose[1]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (340 - h) / 2),
              str(winy_lose[2]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (410 - h) / 2),
              str(winy_lose[3]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (480 - h) / 2),
              str(winy_lose[4]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (550 - h) / 2),
              str(winy_lose[5]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (620 - h) / 2),
              str(winy_lose[6]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (690 - h) / 2),
              str(winy_lose[7]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (760 - h) / 2),
              str(winy_lose[8]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (830 - h) / 2),
              str(winy_lose[9]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (900 - h) / 2),
              str(winy_lose[10]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (970 - h) / 2),
              str(winy_lose[11]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (1050 - h) / 2),
              (str(winy_lose[12]).replace("[", "").replace("'", "").replace("]", "") + " %"),
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (1130 - h) / 2),
              (str(winy_lose[13]).replace("[", "").replace("'", "").replace("]", "") + " %"),
              font=font2, fill="white")

    img.save("statystyki.png")

    conn.commit()
    conn.close()


def statystyki_graczy():
    conn = sqlite3.connect("mapy.db")
    c = conn.cursor()

    img = Image.open(r'staty_graczy_podstawa.png')
    font = ImageFont.truetype("arial.ttf", 30)
    font2 = ImageFont.truetype("arial.ttf", 20)

    c.execute("SELECT nick FROM wynik")
    nick_gracza = c.fetchall()
    c.execute("SELECT czterykille FROM wynik")
    fourk = c.fetchall()
    c.execute("SELECT ace FROM wynik")
    ace = c.fetchall()

    nazwy_graczy = []
    fourky = []
    acey = []

    for nazwa in nick_gracza:
        x = str(nazwa).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        nazwy_graczy.append(x)

    for fourkej in fourk:
        y = str(fourkej).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        fourky.append(y)

    for ejsik in ace:
        z = str(ejsik).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        acey.append(z)

    w, h = font.getsize(str(nazwy_graczy[:1]))
    draw = ImageDraw.Draw(img)
    draw.text(((200 - w) / 2, (56 - h) / 2), "Nick", font=font, fill="white")
    draw.text(((200 - w) / 2, (197 - h) / 2), str(nazwy_graczy[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (300 - h) / 2), str(nazwy_graczy[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (400 - h) / 2), str(nazwy_graczy[2]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (500 - h) / 2), str(nazwy_graczy[3]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (600 - h) / 2), str(nazwy_graczy[4]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((605 - w) / 2, (65 - h) / 2), "4K", font=font, fill="white")
    draw.text(((630 - w) / 2, (197 - h) / 2), str(fourky[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((630 - w) / 2, (297 - h) / 2), str(fourky[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((630 - w) / 2, (397 - h) / 2), str(fourky[2]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((630 - w) / 2, (497 - h) / 2), str(fourky[3]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((630 - w) / 2, (597 - h) / 2), str(fourky[4]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((1000 - w) / 2, (65 - h) / 2), "ACE", font=font, fill="white")
    draw.text(((1050 - w) / 2, (195 - h) / 2), str(acey[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1050 - w) / 2, (295 - h) / 2), str(acey[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1050 - w) / 2, (395 - h) / 2), str(acey[2]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1050 - w) / 2, (495 - h) / 2), str(acey[3]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1050 - w) / 2, (595 - h) / 2), str(acey[4]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    img.save("staty_graczy_gotowe.png")

    conn.commit()
    conn.close()


def stare_mapy():
    conn = sqlite3.connect("mapy.db")
    c = conn.cursor()

    img = Image.open(r'staty_stare.png')
    font = ImageFont.truetype("arial.ttf", 30)
    font2 = ImageFont.truetype("arial.ttf", 20)

    c.execute("SELECT nazwa_starej FROM stare_mapy")
    z = c.fetchall()
    c.execute("SELECT liczba_starej FROM stare_mapy")
    a = c.fetchall()
    c.execute("SELECT win_starej FROM stare_mapy")
    v = c.fetchall()
    c.execute("SELECT lose_starej FROM stare_mapy")
    b = c.fetchall()
    c.execute("SELECT draw_starej FROM stare_mapy")
    n = c.fetchall()
    c.execute("SELECT win_lose_starej FROM stare_mapy")
    m = c.fetchall()

    mapy = []
    liczby = []
    winy = []
    lose = []
    drawy = []
    winy_lose = []

    for mapa in z:
        x = str(mapa).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        mapy.append(x)
    for liczba in a:
        x = str(liczba).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        liczby.append(x)
    for win in v:
        x = str(win).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        winy.append(x)
    for losey in b:
        x = str(losey).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        lose.append(x)
    for drawey in n:
        x = str(drawey).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        drawy.append(x)
    for winyilosy in m:
        x = str(winyilosy).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        winy_lose.append(x)

    w, h = font.getsize(str(mapy[:1]))
    draw = ImageDraw.Draw(img)
    draw.text(((200 - w) / 2, (70 - h) / 2), "Nazwa mapy", font=font, fill="white")
    draw.text(((200 - w) / 2, (200 - h) / 2), str(mapy[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((200 - w) / 2, (270 - h) / 2), str(mapy[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((650 - w) / 2, (75 - h) / 2), "Liczba gier", font=font, fill="white")
    draw.text(((780 - w) / 2, (200 - h) / 2), str(liczby[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((780 - w) / 2, (270 - h) / 2), str(liczby[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((1050 - w) / 2, (75 - h) / 2), "Wygrane", font=font, fill="white")
    draw.text(((1160 - w) / 2, (200 - h) / 2), str(winy[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1160 - w) / 2, (270 - h) / 2), str(winy[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((1400 - w) / 2, (75 - h) / 2), "Przegrane", font=font, fill="white")
    draw.text(((1510 - w) / 2, (200 - h) / 2), str(lose[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1510 - w) / 2, (270 - h) / 2), str(lose[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((1800 - w) / 2, (75 - h) / 2), "Remisy", font=font, fill="white")
    draw.text(((1900 - w) / 2, (200 - h) / 2), str(drawy[0]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")
    draw.text(((1900 - w) / 2, (270 - h) / 2), str(drawy[1]).replace("[", "").replace("'", "").replace("]", ""),
              font=font2, fill="white")

    draw.text(((2150 - w) / 2, (75 - h) / 2), "Win/Lose", font=font, fill="white")
    draw.text(((2240 - w) / 2, (200 - h) / 2),
              str(winy_lose[0]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")
    draw.text(((2240 - w) / 2, (270 - h) / 2),
              str(winy_lose[1]).replace("[", "").replace("'", "").replace("]", "") + " %",
              font=font2, fill="white")

    img.save("statystyki_stare_gotowe.png")

    conn.commit()
    conn.close()


