import random
import sqlite3
import discord
from Robienie_Obrazka import obrazek, statystyki_graczy
from win_lose_ratio import obliczanie_win_lose


TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

num = random.randint(1, 13)
client = discord.Client()

game = discord.Game("Gdzie ten meczmejker?!")


@client.event
async def on_ready():
    print("Zalogowales sie jako: {0.user}".format(client))
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT nazwa FROM mapy WHERE id_mapy=?", (num,))
    mapa = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")

    c.execute("SELECT liczba FROM mapy WHERE id_mapy=?", (num,))
    zagrane_mapy = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")

    if int(zagrane_mapy) == 1:
        cock = " raz"
    else:
        cock = " razy"

    if message.author == client.user:
        return

    if message.content.startswith("^komendy"):
        await message.channel.send("Dostępne komendy to: ^meczmejker, ^staty (już działa!!!), ^premiera, ^mirage, " +
                                   "^nuke, ^dust, ^overpass, ^vertigo, ^ancient, ^train, ^cache, ^mocha, ^office, " +
                                   "^agency, ^inferno, ^prmwin, ^prmlose, ^prmdraw, ^usunwin, ^usunlose, ^usundraw" +
                                   ", ^dodajstaty, ^usunstaty, ^statygraczy")
        await message.channel.send("<:PeepoGlad:815276556863275028>")

    if message.content.startswith('^meczmejker'):
        x = await message.channel.send(
            " <:pogchamp4:809889459944161290> " + "<@&391947653618991106>"
            + "  gramy mape: " +
            mapa + ", gralismy ja: " + zagrane_mapy +
            cock + " <:PeepoGlad:815276556863275028>")
        await x.add_reaction("<:plus1:278220303639904257>")
        await x.add_reaction("<:minus1:278220095447367681>")
        await x.add_reaction("✏️")
        c.execute("""UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=?""", (num,))

    if message.content == "^staty":
        obrazek()
        with open("statystyki.png", "rb") as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

    if message.content == "^statygraczy":
        statystyki_graczy()
        with open("staty_graczy_gotowe.png", "rb") as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)



    if message.content.startswith("^usunstaty"):
        await message.channel.send("Co usunąć ace czy 4k????")

        def check(m):
            return message.author == m.author

        msg = await client.wait_for('message', check=check)
        if msg.content == "ace":
            await message.channel.send("U kogo usunąć ace???")
            def check(m):
                return message.author == m.author

            msg = await client.wait_for('message', check=check)
            if msg.content == "wak":
                c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=1 AND ace>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto ace <:proste:674360939134320640>")

            elif msg.content == "marko":
                c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=2 AND ace>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto ace <:proste:674360939134320640>")

            elif msg.content == "dawid":
                c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=3 AND ace>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto  ace <:proste:674360939134320640>")

            elif msg.content == "jujan":
                c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=4 AND ace>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto ace <:proste:674360939134320640>")

            elif msg.content == "michał":
                c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=4 AND ace>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto 4k <:proste:674360939134320640>")
            else:
                print("afasff")

        elif msg.content == "4k":
            await message.channel.send("U kogo usunąć 4k???")
            def check(m):
                return message.author == m.author

            msg = await client.wait_for('message', check=check)

            if msg.content == "wak":
                c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=1 AND czterykille>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto 4k <:proste:674360939134320640>")

            elif msg.content == "marko":
                c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=2 AND czterykille>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto 4k <:proste:674360939134320640>")

            elif msg.content == "dawid":
                c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=3 AND czterykille>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto 4k <:proste:674360939134320640>")

            elif msg.content == "jujan":
                c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=4 AND czterykille>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto 4k <:proste:674360939134320640>")

            elif msg.content == "michał":
                c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=5 AND czterykille>0")
                conn.commit()
                conn.close()
                await message.channel.send("Usunięto 4k <:proste:674360939134320640>")
            else:
                print("afasff")
        else:
            print("eo")


    if message.content.startswith("^usunlose"):
        await message.channel.send("Z jakiej mapy usunąć lose:")

        def check(m):
            return message.author == m.author

        msg = await client.wait_for('message', check=check)
        if msg.content == "Premiera":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=1 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=1 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(1)
            await message.channel.send("Usunięto przegraną z premiery <:proste:674360939134320640>")
        elif msg.content == "Mirage":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=2 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=2 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(2)
            await message.channel.send("Usunięto przegraną z mirage <:proste:674360939134320640>")
        elif msg.content == "Nuke":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=3 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=3 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(3)
            await message.channel.send("Usunięto przegraną z nuke <:proste:674360939134320640>")
        elif msg.content == "Dust":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=4 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=4 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(4)
            await message.channel.send("Usunięto przegraną z dusta <:proste:674360939134320640>")
        elif msg.content == "Overpass":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=5 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=5 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(5)
            await message.channel.send("Usunięto przegraną z overpassa <:proste:674360939134320640>")
        elif msg.content == "Vertigo":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=6 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=6 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(6)
            await message.channel.send("Usunięto przegraną z vertigo <:proste:674360939134320640>")
        elif msg.content == "Ancient":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=7 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=7 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(7)
            await message.channel.send("Usunięto przegraną z ancient <:proste:674360939134320640>")
        elif msg.content == "Train":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=8 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=8 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(8)
            await message.channel.send("Usunięto przegraną z traina <:proste:674360939134320640>")
        elif msg.content == "Cache":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=9 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=9 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(9)
            await message.channel.send("Usunięto przegraną z cache <:proste:674360939134320640>")
        elif msg.content == "Mocha":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=10 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=10 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(10)
            await message.channel.send("Usunięto przegraną z mocha <:proste:674360939134320640>")
        elif msg.content == "Office":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=11 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=11 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(11)
            await message.channel.send("Usunięto przegraną z office <:proste:674360939134320640>")
        elif msg.content == "Agency":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=12 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=12 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(12)
            await message.channel.send("Usunięto przegraną z agencji <:proste:674360939134320640>")
        elif msg.content == "Inferno":
            c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=13 AND lose>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=13 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(13)
            await message.channel.send("Usunięto przegraną z inferno <:proste:674360939134320640>")
        else:
            print("poop")


    if message.content.startswith("^dodajstaty"):
        await message.channel.send("Kto zrobił ACE/4k ?")

        def check(m):
            return message.author == m.author

        msg = await client.wait_for('message', check=check)
        if msg.content == ("Wak").lower():
            await message.channel.send("ace czy 4k ?")
            msg = await client.wait_for('message', check=check)
            if msg.content == "ace":
                c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=1")
                await message.channel.send("Brawo wak ace :O  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            elif msg.content == "4k":
                c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=1")
                await message.channel.send("Brawo wak 4k  ;)  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            else:
                await message.channel.send("majnkraft")

        elif msg.content == ("Marko").lower():
            await message.channel.send("ace czy 4k ?")
            msg = await client.wait_for('message', check=check)
            if msg.content == "ace":
                c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=2")
                await message.channel.send("Brawo marko ace :O  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            elif msg.content == "4k":
                c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=2")
                await message.channel.send("Brawo marko 4k  ;)  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            else:
                await message.channel.send("majnkraft")

        elif msg.content == ("Dawid").lower():
            await message.channel.send("ace czy 4k ?")
            msg = await client.wait_for('message', check=check)
            if msg.content == "ace":
                c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=3")
                await message.channel.send("Brawo dawid ace :O  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            elif msg.content == "4k":
                c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=3")
                await message.channel.send("Brawo dawid 4k  ;)  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            else:
                await message.channel.send("majnkraft")

        elif msg.content == ("Jujan").lower():
            await message.channel.send("ace czy 4k ?")
            msg = await client.wait_for('message', check=check)
            if msg.content == "ace":
                c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=4")
                await message.channel.send("Brawo jujen ace :O  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            elif msg.content == "4k":
                c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=4")
                await message.channel.send("Brawo jujen 4k  ;)  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            else:
                await message.channel.send("majnkraft")

        elif msg.content == ("Michał").lower():
            await message.channel.send("ace czy 4k ?")
            msg = await client.wait_for('message', check=check)
            if msg.content == "ace":
                c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=5")
                await message.channel.send("Brawo miszello ace :O  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            elif msg.content == "4k":
                c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=5")
                await message.channel.send("Brawo miszello 4k  ;)  <:pogchamp4:809889459944161290>")
                conn.commit()
                conn.close()
            else:
                await message.channel.send("majnkraft")
        else:
            print("popopo")


    if message.content.startswith("^michal"):
        with open("michal.png", "rb") as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)


    if message.content.startswith("^usunwin"):
        await message.channel.send("Z jakiej mapy usunąć wina:")

        def check(m):
            return message.author == m.author

        msg = await client.wait_for('message', check=check)
        if msg.content == "Premiera":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=1 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=1 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(1)
            await message.channel.send("Usunięto wygraną z premiery <:proste:674360939134320640>")
        elif msg.content == "Mirage":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=2 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=2 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(2)
            await message.channel.send("Usunięto wygraną z mirage <:proste:674360939134320640>")
        elif msg.content == "Nuke":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=3 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=3 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(3)
            await message.channel.send("Usunięto wygraną z nuke <:proste:674360939134320640>")
        elif msg.content == "Dust":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=4 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=4 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(4)
            await message.channel.send("Usunięto wygraną z dusta <:proste:674360939134320640>")
        elif msg.content == "Overpass":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=5 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=5 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(5)
            await message.channel.send("Usunięto wygraną z overpassa <:proste:674360939134320640>")
        elif msg.content == "Vertigo":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=6 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=6 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(6)
            await message.channel.send("Usunięto wygraną z vertigo <:proste:674360939134320640>")
        elif msg.content == "Ancient":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=7 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=7 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(7)
            await message.channel.send("Usunięto wygraną z ancient <:proste:674360939134320640>")
        elif msg.content == "Train":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=8 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=8 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(8)
            await message.channel.send("Usunięto wygraną z traina <:proste:674360939134320640>")
        elif msg.content == "Cache":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=9 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=9 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(9)
            await message.channel.send("Usunięto wygraną z cache <:proste:674360939134320640>")
        elif msg.content == "Mocha":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=10 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=10 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(10)
            await message.channel.send("Usunięto wygraną z mocha <:proste:674360939134320640>")
        elif msg.content == "Office":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=11 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=11 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(11)
            await message.channel.send("Usunięto wygraną z office <:proste:674360939134320640>")
        elif msg.content == "Agency":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=12 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=12 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(12)
            await message.channel.send("Usunięto wygraną z agencji <:proste:674360939134320640>")
        elif msg.content == "Inferno":
            c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=13 AND win>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=13 AND liczba>0")
            conn.commit()
            conn.close()
            obliczanie_win_lose(13)
            await message.channel.send("Usunięto wygraną z inferno <:proste:674360939134320640>")
        else:
            print("poop")

    if message.content.startswith("^usundraw"):
        await message.channel.send("Z jakiej mapy usunąć remis:")

        def check(m):
            return message.author == m.author

        msg = await client.wait_for('message', check=check)
        if msg.content == "Premiera":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=1 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=1 AND liczba>0")
            await message.channel.send("Usunięto remis z premiery <:proste:674360939134320640>")
        elif msg.content == "Mirage":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=2 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=2 AND liczba>0")
            await message.channel.send("Usunięto remis z mirage <:proste:674360939134320640>")
        elif msg.content == "Nuke":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=3 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=3 AND liczba>0")
            await message.channel.send("Usunięto remis z nuke <:proste:674360939134320640>")
        elif msg.content == "Dust":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=4 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=4 AND liczba>0")
            await message.channel.send("Usunięto remis z dusta <:proste:674360939134320640>")
        elif msg.content == "Overpass":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=5 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=5 AND liczba>0")
            await message.channel.send("Usunięto remis z overpassa <:proste:674360939134320640>")
        elif msg.content == "Vertigo":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=6 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=6 AND liczba>0")
            await message.channel.send("Usunięto remis z vertigo <:proste:674360939134320640>")
        elif msg.content == "Ancient":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=7 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=7 AND liczba>0")
            await message.channel.send("Usunięto remis z ancient <:proste:674360939134320640>")
        elif msg.content == "Train":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=8 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=8 AND liczba>0")
            await message.channel.send("Usunięto remis z traina <:proste:674360939134320640>")
        elif msg.content == "Cache":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=9 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=9 AND liczba>0")
            await message.channel.send("Usunięto remis z cache <:proste:674360939134320640>")
        elif msg.content == "Mocha":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=10 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=10 AND liczba>0")
            await message.channel.send("Usunięto remis z mocha <:proste:674360939134320640>")
        elif msg.content == "Office":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=11 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=11 AND liczba>0")
            await message.channel.send("Usunięto remis z office <:proste:674360939134320640>")
        elif msg.content == "Agency":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=12 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=12 AND liczba>0")
            await message.channel.send("Usunięto remis z agencji <:proste:674360939134320640>")
        elif msg.content == "Inferno":
            c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=13 AND draw>0")
            c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=13 AND liczba>0")
            await message.channel.send("Usunięto remis z inferno <:proste:674360939134320640>")
        else:
            print("poop")

    if message.content.startswith('^premiera'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=1")
        prm = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(prm) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=1")
        prm = await message.channel.send(
            "Dzisiaj Premiera " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", tryb gralismy: " + prm + " " + booba + " <:PeepoGlad:815276556863275028>")
        await message.channel.send("Jaka mapa grana wariacie: ^mirage, ^nuke, ^overpass, ^dust, ^inferno, ^vertigo " +
                                   "^ancient")
        conn.commit()
        conn.close()

    if message.content.startswith("^prmwin"):
        c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=1")
        conn.commit()
        conn.close()
        obliczanie_win_lose(1)
        await message.channel.send("Wygranko premiery " + "<:PeepoGlad:815276556863275028>")

    if message.content.startswith("^prmlose"):
        c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=1")
        conn.commit()
        conn.close()
        obliczanie_win_lose(1)
        await message.channel.send("Przegranko premiery " + "<:Pepe:236556210508136458>")

    if message.content.startswith("^prmdraw"):
        c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=1")
        conn.commit()
        conn.close()
        await message.channel.send("Remis premiery " + "<:yep:676891566513717248>")

    if message.content.startswith('^mirage'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=2")
        mrg = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(mrg) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=2")
        mir = await message.channel.send(
            "Dzisiaj Mirage " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + mrg + " " + booba + " <:PeepoGlad:815276556863275028>")
        await mir.add_reaction("<:plus1:278220303639904257>")
        await mir.add_reaction("<:minus1:278220095447367681>")
        await mir.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^nuke'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=3")
        nke = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(nke) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=3")
        nke = await message.channel.send(
            "Dzisiaj Nuke " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + nke + " " + booba + " <:PeepoGlad:815276556863275028>")
        await nke.add_reaction("<:plus1:278220303639904257>")
        await nke.add_reaction("<:minus1:278220095447367681>")
        await nke.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^dust'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=4")
        dd = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(dd) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=4")
        dd = await message.channel.send(
            "Dzisiaj Mapa Majkela " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + dd + " " + booba + " <:PeepoGlad:815276556863275028>")
        await dd.add_reaction("<:plus1:278220303639904257>")
        await dd.add_reaction("<:minus1:278220095447367681>")
        await dd.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^overpass'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=5")
        ovp = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(ovp) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=5")
        ovp = await message.channel.send(
            "Dzisiaj Overpass " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + ovp + " " + booba + " <:PeepoGlad:815276556863275028>")
        await ovp.add_reaction("<:plus1:278220303639904257>")
        await ovp.add_reaction("<:minus1:278220095447367681>")
        await ovp.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^vertigo'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=6")
        vrt = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(vrt) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=6")
        vrt = await message.channel.send(
            "Dzisiaj Vertigo " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + vrt + " " + booba + " <:PeepoGlad:815276556863275028>")
        await vrt.add_reaction("<:plus1:278220303639904257>")
        await vrt.add_reaction("<:minus1:278220095447367681>")
        await vrt.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^ancient'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=7")
        anc = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(anc) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=7")
        anc = await message.channel.send(
            "Dzisiaj Ancient " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + anc + " " + booba + " <:PeepoGlad:815276556863275028>")
        await anc.add_reaction("<:plus1:278220303639904257>")
        await anc.add_reaction("<:minus1:278220095447367681>")
        await anc.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^train'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=8")
        trn = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(trn) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=8")
        trn = await message.channel.send(
            "Dzisiaj Pociong " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + trn + " " + booba + " <:PeepoGlad:815276556863275028>")
        await trn.add_reaction("<:plus1:278220303639904257>")
        await trn.add_reaction("<:minus1:278220095447367681>")
        await trn.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^cache'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=9")
        cch = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(cch) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=9")
        cch = await message.channel.send(
            "Dzisiaj Keszyk " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + cch + " " + booba + " <:PeepoGlad:815276556863275028>")
        await cch.add_reaction("<:plus1:278220303639904257>")
        await cch.add_reaction("<:minus1:278220095447367681>")
        await cch.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^mocha'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=10")
        moc = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(moc) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=10")
        moc = await message.channel.send(
            "Dzisiaj Mocha " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + moc + " " + booba + " <:PeepoGlad:815276556863275028>")
        await moc.add_reaction("<:plus1:278220303639904257>")
        await moc.add_reaction("<:minus1:278220095447367681>")
        await moc.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^office'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=11")
        off = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(off) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=11")
        off = await message.channel.send(
            "Dzisiaj Office " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + off + " " + booba + " <:PeepoGlad:815276556863275028>")
        await off.add_reaction("<:plus1:278220303639904257>")
        await off.add_reaction("<:minus1:278220095447367681>")
        await off.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^agency'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=12")
        agc = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(agc) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=12")
        agc = await message.channel.send(
            "Dzisiaj Agencja " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + agc + " " + booba + " <:PeepoGlad:815276556863275028>")
        await agc.add_reaction("<:plus1:278220303639904257>")
        await agc.add_reaction("<:minus1:278220095447367681>")
        await agc.add_reaction("✏️")
        conn.commit()
        conn.close()

    if message.content.startswith('^inferno'):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=13")
        inf = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
        if int(inf) == 1:
            booba = "raz"
        else:
            booba = "razy"
        c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=13")
        inf = await message.channel.send(
            "Dzisiaj Inferno " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
            + ", mape gralismy: " + inf + " " + booba + " <:PeepoGlad:815276556863275028>")
        await inf.add_reaction("<:plus1:278220303639904257>")
        await inf.add_reaction("<:minus1:278220095447367681>")
        await inf.add_reaction("✏️")
        conn.commit()
        conn.close()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                if message.content.startswith("^meczmejker"):
                    c.execute("""UPDATE mapy SET win=win+1 WHERE id_mapy=?""", (num,))
                    c.execute("SELECT nazwa FROM mapy WHERE id_mapy=?", (num,))
                    m = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
                    conn.commit()
                    conn.close()
                    await x.delete()
                    await message.channel.send("Wygranko: " + m + " " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(num)
                elif message.content.startswith("^premiera"):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=1")
                    conn.commit()
                    conn.close()
                    await prm.delete()
                    await message.channel.send("Wygranko: Premiera " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(1)
                elif message.content.startswith('^mirage'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=2")
                    conn.commit()
                    conn.close()
                    await mir.delete()
                    await message.channel.send("Wygranko: Mirage " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(2)
                elif message.content.startswith('^nuke'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=3")
                    conn.commit()
                    conn.close()
                    await nke.delete()
                    await message.channel.send("Wygranko: Nuke " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(3)
                elif message.content.startswith('^dust'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=4")
                    conn.commit()
                    conn.close()
                    await dd.delete()
                    await message.channel.send("Wygranko: Dust " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(4)
                elif message.content.startswith('^overpass'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=5")
                    conn.commit()
                    conn.close()
                    await ovp.delete()
                    await message.channel.send("Wygranko: Overpass " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(5)
                elif message.content.startswith('^vertigo'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=6")
                    conn.commit()
                    conn.close()
                    await vrt.delete()
                    await message.channel.send("Wygranko: Vertigo " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(6)
                elif message.content.startswith('^ancient'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=7")
                    conn.commit()
                    conn.close()
                    await anc.delete()
                    await message.channel.send("Wygranko: Ancient " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(7)
                elif message.content.startswith('^train'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=8")
                    conn.commit()
                    conn.close()
                    await trn.delete()
                    await message.channel.send("Wygranko: Train " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(8)
                elif message.content.startswith('^cache'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=9")
                    conn.commit()
                    conn.close()
                    await cch.delete()
                    await message.channel.send("Wygranko: Cache " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(9)
                elif message.content.startswith('^mocha'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=10")
                    conn.commit()
                    conn.close()
                    await moc.delete()
                    await message.channel.send("Wygranko: Mocha " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(10)
                elif message.content.startswith('^office'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=11")
                    conn.commit()
                    conn.close()
                    await off.delete()
                    await message.channel.send("Wygranko: Office " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(11)
                elif message.content.startswith('^agency'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=12")
                    conn.commit()
                    conn.close()
                    await agc.delete()
                    await message.channel.send("Wygranko: Agency " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(12)
                elif message.content.startswith('^inferno'):
                    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=13")
                    conn.commit()
                    conn.close()
                    await inf.delete()
                    await message.channel.send("Wygranko: Inferno " + "<:proste:674360939134320640>")
                    obliczanie_win_lose(13)
                else:
                    print("EO")
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                if message.content.startswith("^meczmejker"):
                    c.execute("""UPDATE mapy SET lose=lose+1 WHERE id_mapy=?""", (num,))
                    conn.commit()
                    conn.close()
                    await x.delete()
                    await message.channel.send("Przegranko " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(num)
                if message.content.startswith('^premiera'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=1")
                    conn.commit()
                    conn.close()
                    await prm.delete()
                    await message.channel.send("Przegranko: Premiera " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(1)
                if message.content.startswith('^mirage'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=2")
                    conn.commit()
                    conn.close()
                    await mir.delete()
                    await message.channel.send("Przegranko: Mirage " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(2)
                if message.content.startswith('^nuke'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=3")
                    conn.commit()
                    conn.close()
                    await nke.delete()
                    await message.channel.send("Przegranko: Nuke " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(3)
                if message.content.startswith('^dust'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=4")
                    conn.commit()
                    conn.close()
                    await dd.delete()
                    await message.channel.send("Przegranko: Dust " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(4)
                if message.content.startswith('^overpass'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=5")
                    conn.commit()
                    conn.close()
                    await ovp.delete()
                    await message.channel.send("Przegranko: Overpass " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(5)
                if message.content.startswith('^vertigo'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=6")
                    conn.commit()
                    conn.close()
                    await vrt.delete()
                    await message.channel.send("Przegranko: Vertigo " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(6)
                if message.content.startswith('^ancient'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=7")
                    conn.commit()
                    conn.close()
                    await anc.delete()
                    await message.channel.send("Przegranko: Ancient " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(7)
                if message.content.startswith('^train'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=8")
                    conn.commit()
                    conn.close()
                    await trn.delete()
                    await message.channel.send("Przegranko: Train " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(8)
                if message.content.startswith('^cache'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=9")
                    conn.commit()
                    conn.close()
                    await cch.delete()
                    await message.channel.send("Przegranko: Cache " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(9)
                if message.content.startswith('^mocha'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=10")
                    conn.commit()
                    conn.close()
                    await moc.delete()
                    await message.channel.send("Przegranko: Mocha " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(10)
                if message.content.startswith('^office'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=11")
                    conn.commit()
                    conn.close()
                    await off.delete()
                    await message.channel.send("Przegranko: Office " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(11)
                if message.content.startswith('^agency'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=12")
                    conn.commit()
                    conn.close()
                    await agc.delete()
                    await message.channel.send("Przegranko: Agency " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(12)
                if message.content.startswith('^inferno'):
                    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=13")
                    conn.commit()
                    conn.close()
                    await inf.delete()
                    await message.channel.send("Przegranko: Inferno " + "<:Pepe:236556210508136458>")
                    obliczanie_win_lose(13)
            if str(reaction.emoji) == "✏️":
                if message.content.startswith("^meczmejker"):
                    c.execute("""UPDATE mapy SET draw=draw+1 WHERE id_mapy=?""", (num,))
                    await x.delete()
                    await message.channel.send("Remis " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^premiera'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=1")
                    await prm.delete()
                    await message.channel.send("Remis: Premiera " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^mirage'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=2")
                    await mir.delete()
                    await message.channel.send("Remis: Mirage " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^nuke'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=3")
                    await nke.delete()
                    await message.channel.send("Remis: Nuke " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^dust'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=4")
                    await dd.delete()
                    await message.channel.send("Remis: Dust " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^overpass'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=5")
                    await ovp.delete()
                    await message.channel.send("Remis: Overpass " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^vertigo'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=6")
                    await vrt.delete()
                    await message.channel.send("Remis: Vertigo " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^ancient'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=7")
                    await anc.delete()
                    await message.channel.send("Remis: Ancient " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^train'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=8")
                    await trn.delete()
                    await message.channel.send("Remis: Train " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^cache'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=9")
                    await cch.delete()
                    await message.channel.send("Remis: Cache " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^mocha'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=10")
                    await moc.delete()
                    await message.channel.send("Remis: Mocha " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^office'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=11")
                    await off.delete()
                    await message.channel.send("Remis: Office " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^agency'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=12")
                    await agc.delete()
                    await message.channel.send("Remis: Agency " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                elif message.content.startswith('^inferno'):
                    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=13")
                    await inf.delete()
                    await message.channel.send("Remis: Inferno " + "<:Omegalul:428861885111205888>")
                    conn.commit()
                    conn.close()
                else:
                    print("oddychac")


client.run(TOKEN)
