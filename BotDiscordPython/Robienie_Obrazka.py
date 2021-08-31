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
    draw.text(((200 - w) / 2, (1040 - h) / 2), str(mapy[12]).replace("[", "").replace("'", "").replace("]", ""),
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
    draw.text(((780 - w) / 2, (1040 - h) / 2), str(liczby[12]).replace("[", "").replace("'", "").replace("]", ""),
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
    draw.text(((1160 - w) / 2, (1040 - h) / 2), str(winy[12]).replace("[", "").replace("'", "").replace("]", ""),
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
    draw.text(((1510 - w) / 2, (1040 - h) / 2), str(lose[12]).replace("[", "").replace("'", "").replace("]", ""),
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
    draw.text(((1900 - w) / 2, (1040 - h) / 2), str(drawy[12]).replace("[", "").replace("'", "").replace("]", ""),
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
    draw.text(((2240 - w) / 2, (1040 - h) / 2),
              (str(winy_lose[12]).replace("[", "").replace("'", "").replace("]", "") + " %"),
              font=font2, fill="white")

    img.save("statystyki.png")

    conn.commit()
    conn.close()
