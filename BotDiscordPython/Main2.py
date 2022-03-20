import sqlite3
import discord
from discord.ext import commands
from Robienie_Obrazka import obrazek, statystyki_graczy, stare_mapy
from win_lose_ratio import obliczanie_win_lose, obliczanie_stare_win_lose
from Database_backup import backup_bazy
import json
from steam.webapi import WebAPI

with open("steamapitoken.txt") as f:
    key = f.read().strip()

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()


client = commands.Bot(command_prefix='^')
game = discord.Game("Gdzie ten meczmejker?!")


@client.event
async def on_ready():
    print("Zalogowales sie jako: {0.user}".format(client))
    await client.change_presence(activity=game)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def komendy(ctx):
    await ctx.channel.send(
        "Dostępne komendy to: ^staty, ^premiera, ^mirage, ^nuke, ^dust, ^overpass, ^vertigo, ^ancient, ^train, "
        "^cache, ^office, ^agency, ^inferno, ^iris, ^climb, ^prmwin, ^prmlose, ^prmdraw, ^usunwin, ^usunlose, "
        "^usundraw, ^dodajstaty, ^usunstaty, ^statygraczy, ^odswiez, ^starestaty, ^czygra, ^slots")
    await ctx.channel.send("<:PeepoGlad:815276556863275028>")


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def czygra(ctx):
    lista = []
    await ctx.send("Podaj SteamID")
    def check(m):
        return m.author.id == ctx.author.id
    message = await client.wait_for('message', check=check)
    api = WebAPI(key=key)
    x = api.ISteamUser.GetPlayerSummaries(steamids=str(message.content))
    with open('isplaying.json', 'w', encoding='utf-8') as f:
        json.dump(x, f, ensure_ascii=False, indent=4)
    with open('isplaying.json') as jsonFile1:
        jsonObject1 = json.load(jsonFile1)
        jsonFile1.close()
    res1 = jsonObject1['response']
    player1 = res1['players']
    for value1 in player1:
        for item1 in value1.values():
            lista.append(item1)
    if 'Counter-Strike: Global Offensive' in lista:
        await ctx.channel.send(lista[3] + " gra w CS:GO (OSTROŻNIE)")
    if 'Counter-Strike: Global Offensive' not in lista:
        await ctx.channel.send(lista[3] + " nie gra w CS:GO (GRANKO)")


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def staty(ctx):
    obrazek()
    with open("statystyki.png", "rb") as f:
        picture = discord.File(f)
        await ctx.channel.send(file=picture)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def starestaty(ctx):
    stare_mapy()
    with open("statystyki_stare_gotowe.png", "rb") as f:
        picture = discord.File(f)
        await ctx.channel.send(file=picture)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def statygraczy(ctx):
    statystyki_graczy()
    with open("staty_graczy_gotowe.png", "rb") as f:
        picture = discord.File(f)
        await ctx.channel.send(file=picture)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def michal(ctx):
    with open("michal.png", "rb") as f:
        picture = discord.File(f)
        await ctx.channel.send(file=picture)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def odswiez(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    for z in range(1, 3):
        obliczanie_stare_win_lose(z)

    for x in range(1, 15):
        c.execute("SELECT liczba FROM mapy WHERE id_mapy=?", (x,))
        l = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        c.execute("SELECT nazwa FROM mapy WHERE id_mapy=?", (x,))
        o = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")
        if int(l) > 0:
            obliczanie_win_lose(x)
        else:
            await ctx.channel.send("Nie odświeżono mapy o nazwie " + o + " poniewaz liczba gier wynosi 0")

    await ctx.channel.send("Odświeżono win/lose ratio na reszcie map  <:pogchamp4:809889459944161290>")
    conn.commit()
    conn.close()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def usunstaty(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    await ctx.channel.send("Co usunąć ace czy 4k????")

    def check(m):
        return ctx.author == m.author

    msg = await client.wait_for('message', check=check)
    if msg.content == "ace":
        await ctx.channel.send("U kogo usunąć ace???")

        def check(m):
            return ctx.author == m.author

        msg = await client.wait_for('message', check=check)
        if msg.content.lower() == "wak" or msg.content.lower() == "vaq":
            c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=1 AND ace>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto ace <:proste:674360939134320640>")

        elif msg.content.lower() == "marko" or msg.content.lower() == "makro" or msg.content.lower() == "marek":
            c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=2 AND ace>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto ace <:proste:674360939134320640>")

        elif msg.content.lower() == "dawid":
            c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=3 AND ace>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto  ace <:proste:674360939134320640>")

        elif msg.content.lower() == "jujan" or msg.content.lower() == "radek":
            c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=4 AND ace>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto ace <:proste:674360939134320640>")

        elif msg.content.lower() == "michał" or msg.content.lower() == "michal" or msg.content.lower() == "shir":
            c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=5 AND ace>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto ace <:proste:674360939134320640>")

        elif msg.content.lower() == "elektro" or msg.content.lower() == "elektroencefalograf" or msg.content.lower() == "hesus":
            c.execute("UPDATE wynik SET ace=ace-1 WHERE id_wyniku=6 AND ace>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto ace <:proste:674360939134320640>")
        else:
            print("error ace")

    elif msg.content == "4k":
        await ctx.channel.send("U kogo usunąć 4k???")

        def check(m):
            return ctx.author == m.author

        msg = await client.wait_for('message', check=check)

        if msg.content.lower() == "wak" or msg.content.lower() == "vaq":
            c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=1 AND czterykille>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto 4k <:proste:674360939134320640>")

        elif msg.content.lower() == "marko" or msg.content.lower() == "makro" or msg.content.lower() == "marek":
            c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=2 AND czterykille>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto 4k <:proste:674360939134320640>")

        elif msg.content.lower() == "dawid":
            c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=3 AND czterykille>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto 4k <:proste:674360939134320640>")

        elif msg.content.lower() == "jujan" or msg.content.lower() == "radek":
            c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=4 AND czterykille>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto 4k <:proste:674360939134320640>")

        elif msg.content.lower() == "michał" or msg.content.lower() == "michal" or msg.content.lower() == "shir":
            c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=5 AND czterykille>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto 4k <:proste:674360939134320640>")

        elif msg.content.lower() == "elektro" or msg.content.lower() == "elektroencefalograf" or msg.content.lower() == "hesus":
            c.execute("UPDATE wynik SET czterykille=czterykille-1 WHERE id_wyniku=6 AND czterykille>0")
            conn.commit()
            conn.close()
            backup_bazy()
            await ctx.channel.send("Usunięto 4k <:proste:674360939134320640>")
        else:
            print("error 4k")
    else:
        print("error ace/4k")

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def dodajstaty(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    await ctx.channel.send("Kto zrobił ACE/4k ?")

    def check(m):
        return ctx.author == m.author

    msg = await client.wait_for('message', check=check)
    if msg.content.lower() == "wak" or msg.content.lower() == "vaq":
        await ctx.channel.send("ace czy 4k ?")
        msg = await client.wait_for('message', check=check)
        if msg.content == "ace":
            c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=1")
            await ctx.channel.send("Brawo wak ace :O  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        elif msg.content == "4k":
            c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=1")
            await ctx.channel.send("Brawo wak 4k  ;)  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        else:
            print("error dodajstaty user")

    elif msg.content.lower() == "marko" or msg.content.lower() == "makro" or msg.content.lower() == "marek":
        await ctx.channel.send("ace czy 4k ?")
        msg = await client.wait_for('message', check=check)
        if msg.content == "ace":
            c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=2")
            await ctx.channel.send("Brawo marko ace :O  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        elif msg.content == "4k":
            c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=2")
            await ctx.channel.send("Brawo marko 4k  ;)  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        else:
            print("error dodajstaty user")

    elif msg.content.lower() == "dawid":
        await ctx.channel.send("ace czy 4k ?")
        msg = await client.wait_for('message', check=check)
        if msg.content == "ace":
            c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=3")
            await ctx.channel.send("Brawo dawid ace :O  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        elif msg.content == "4k":
            c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=3")
            await ctx.channel.send("Brawo dawid 4k  ;)  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        else:
            print("error dodajstaty user")

    elif msg.content.lower() == "jujan" or msg.content.lower() == "radek":
        await ctx.channel.send("ace czy 4k ?")
        msg = await client.wait_for('message', check=check)
        if msg.content == "ace":
            c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=4")
            await ctx.channel.send("Brawo jujen ace :O  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        elif msg.content == "4k":
            c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=4")
            await ctx.channel.send("Brawo jujen 4k  ;)  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        else:
            print("error dodaj staty user")

    elif msg.content.lower() == "michał" or msg.content.lower() == "michal" or msg.content.lower() == "shir":
        await ctx.channel.send("ace czy 4k ?")
        msg = await client.wait_for('message', check=check)
        if msg.content == "ace":
            c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=5")
            await ctx.channel.send("Brawo miszello ace :O  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        elif msg.content == "4k":
            c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=5")
            await ctx.channel.send("Brawo miszello 4k  ;)  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
    elif msg.content.lower() == "elektro" or msg.content.lower() == "elektroencefalograf" or msg.content.lower() == "hesus":
        await ctx.channel.send("ace czy 4k ?")
        msg = await client.wait_for('message', check=check)
        if msg.content == "ace":
            c.execute("UPDATE wynik SET ace=ace+1 WHERE id_wyniku=6")
            await ctx.channel.send("Brawo elektro ace :O  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()
        elif msg.content == "4k":
            c.execute("UPDATE wynik SET czterykille=czterykille+1 WHERE id_wyniku=6")
            await ctx.channel.send("Brawo elektro 4k  ;)  <:pogchamp4:809889459944161290>")
            conn.commit()
            conn.close()
            backup_bazy()

    else:
        print("error")

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def usunlose(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    await ctx.channel.send("Z jakiej mapy usunąć lose:")

    def check(m):
        return ctx.author == m.author

    msg = await client.wait_for('message', check=check)
    if msg.content.startswith("Premiera"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=1 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=1 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(1)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z premiery <:proste:674360939134320640>")
    elif msg.content.startswith("Mirage"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=2 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=2 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(2)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z mirage <:proste:674360939134320640>")
    elif msg.content.startswith("Nuke"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=3 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=3 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(3)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z nuke <:proste:674360939134320640>")
    elif msg.content.startswith("Dust"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=4 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=4 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(4)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z dusta <:proste:674360939134320640>")
    elif msg.content.startswith("Overpass"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=5 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=5 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(5)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z overpassa <:proste:674360939134320640>")
    elif msg.content.startswith("Vertigo"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=6 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=6 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(6)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z vertigo <:proste:674360939134320640>")
    elif msg.content.startswith("Ancient"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=7 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=7 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(7)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z ancient <:proste:674360939134320640>")
    elif msg.content.startswith("Train"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=8 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=8 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(8)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z traina <:proste:674360939134320640>")
    elif msg.content.startswith("Cache"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=9 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=9 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(9)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z cache <:proste:674360939134320640>")
    elif msg.content.startswith("Iris"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=10 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=10 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(10)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z iris <:proste:674360939134320640>")
    elif msg.content.startswith("Office"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=11 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=11 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(11)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z office <:proste:674360939134320640>")
    elif msg.content.startswith("Agency"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=12 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=12 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(12)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z agencji <:proste:674360939134320640>")
    elif msg.content.startswith("Inferno"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=13 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=13 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(13)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z inferno <:proste:674360939134320640>")
    elif msg.content.startswith("Climb"):
        c.execute("UPDATE mapy SET lose=lose-1 WHERE id_mapy=14 AND lose>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=14 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(14)
        backup_bazy()
        await ctx.channel.send("Usunięto przegraną z climb <:proste:674360939134320640>")
    else:
        print("error usunlose")


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def usunwin(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    await ctx.channel.send("Z jakiej mapy usunąć wina:")

    def check(m):
        return ctx.author == m.author

    msg = await client.wait_for('message', check=check)
    if msg.content.startswith("Premiera"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=1 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=1 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(1)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z premiery <:proste:674360939134320640>")
    elif msg.content.startswith("Mirage"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=2 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=2 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(2)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z mirage <:proste:674360939134320640>")
    elif msg.content.startswith("Nuke"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=3 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=3 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(3)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z nuke <:proste:674360939134320640>")
    elif msg.content.startswith("Dust"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=4 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=4 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(4)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z dusta <:proste:674360939134320640>")
    elif msg.content.startswith("Overpass"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=5 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=5 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(5)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z overpassa <:proste:674360939134320640>")
    elif msg.content.startswith("Vertigo"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=6 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=6 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(6)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z vertigo <:proste:674360939134320640>")
    elif msg.content.startswith("Ancient"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=7 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=7 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(7)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z ancient <:proste:674360939134320640>")
    elif msg.content.startswith("Train"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=8 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=8 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(8)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z traina <:proste:674360939134320640>")
    elif msg.content.startswith("Cache"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=9 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=9 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(9)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z cache <:proste:674360939134320640>")
    elif msg.content.startswith("Iris"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=10 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=10 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(10)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z iris <:proste:674360939134320640>")
    elif msg.content.startswith("Office"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=11 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=11 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(11)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z office <:proste:674360939134320640>")
    elif msg.content.startswith("Agency"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=12 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=12 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(12)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z agencji <:proste:674360939134320640>")
    elif msg.content.startswith("Inferno"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=13 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=13 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(13)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z inferno <:proste:674360939134320640>")
    elif msg.content.startswith("Climb"):
        c.execute("UPDATE mapy SET win=win-1 WHERE id_mapy=14 AND win>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=14 AND liczba>0")
        conn.commit()
        conn.close()
        obliczanie_win_lose(14)
        backup_bazy()
        await ctx.channel.send("Usunięto wygraną z climb <:proste:674360939134320640>")
    else:
        print("error usunwin")


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def usundraw(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    await ctx.channel.send("Z jakiej mapy usunąć remis:")

    def check(m):
        return ctx.author == m.author

    msg = await client.wait_for('message', check=check)
    if msg.content.startswith("Premiera"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=1 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=1 AND liczba>0")
        await ctx.channel.send("Usunięto remis z premiery <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Mirage"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=2 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=2 AND liczba>0")
        await ctx.channel.send("Usunięto remis z mirage <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Nuke"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=3 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=3 AND liczba>0")
        await ctx.channel.send("Usunięto remis z nuke <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Dust"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=4 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=4 AND liczba>0")
        await ctx.channel.send("Usunięto remis z dusta <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Overpass"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=5 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=5 AND liczba>0")
        await ctx.channel.send("Usunięto remis z overpassa <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Vertigo"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=6 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=6 AND liczba>0")
        await ctx.channel.send("Usunięto remis z vertigo <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Ancient"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=7 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=7 AND liczba>0")
        await ctx.channel.send("Usunięto remis z ancient <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Train"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=8 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=8 AND liczba>0")
        await ctx.channel.send("Usunięto remis z traina <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Cache"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=9 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=9 AND liczba>0")
        await ctx.channel.send("Usunięto remis z cache <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Iris"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=10 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=10 AND liczba>0")
        await ctx.channel.send("Usunięto remis z iris <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Office"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=11 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=11 AND liczba>0")
        await ctx.channel.send("Usunięto remis z office <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Agency"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=12 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=12 AND liczba>0")
        await ctx.channel.send("Usunięto remis z agencji <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Inferno"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=13 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=13 AND liczba>0")
        await ctx.channel.send("Usunięto remis z inferno <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    elif msg.content.startswith("Climb"):
        c.execute("UPDATE mapy SET draw=draw-1 WHERE id_mapy=14 AND draw>0")
        c.execute("UPDATE mapy SET liczba=liczba-1 WHERE id_mapy=14 AND liczba>0")
        await ctx.channel.send("Usunięto remis z climb <:proste:674360939134320640>")
        conn.commit()
        conn.close()
        backup_bazy()
    else:
        print("error usundraw")


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def premiera(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=1")
    prm = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(prm) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=1")
    prm = await ctx.channel.send(
        "Dzisiaj Premiera " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", tryb gralismy: " + prm + " " + booba + " <:PeepoGlad:815276556863275028>")
    await ctx.channel.send("Jaka mapa grana wariacie: ^mirage, ^nuke, ^overpass, ^dust, ^inferno, ^vertigo " +
                               "^ancient")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=1")
                conn.commit()
                conn.close()
                await prm.delete()
                await ctx.channel.send("Wygranko: Premiera " + "<:proste:674360939134320640>")
                obliczanie_win_lose(1)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=1")
                conn.commit()
                conn.close()
                await prm.delete()
                await ctx.channel.send("Przegranko: Premiera " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(1)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=1")
                await prm.delete()
                await ctx.channel.send("Remis: Premiera " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def prmwin(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=1")
    conn.commit()
    conn.close()
    obliczanie_win_lose(1)
    backup_bazy()
    await ctx.channel.send("Wygranko premiery " + "<:PeepoGlad:815276556863275028>")


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def prmlose(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=1")
    conn.commit()
    conn.close()
    obliczanie_win_lose(1)
    backup_bazy()
    await ctx.channel.send("Przegranko premiery " + "<:Pepe:236556210508136458>")

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def prmdraw(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=1")
    conn.commit()
    conn.close()
    backup_bazy()
    await ctx.channel.send("Remis premiery " + "<:yep:676891566513717248>")

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def mirage(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy = 2")
    mrg = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(mrg) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=2")
    mir = await ctx.channel.send(
        "Dzisiaj Mirage " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + mrg + " " + booba + " <:PeepoGlad:815276556863275028>")
    await mir.add_reaction("<:plus1:278220303639904257>")
    await mir.add_reaction("<:minus1:278220095447367681>")
    await mir.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=2")
                conn.commit()
                conn.close()
                await mir.delete()
                await ctx.channel.send("Wygranko: Mirage " + "<:proste:674360939134320640>")
                obliczanie_win_lose(2)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=2")
                conn.commit()
                conn.close()
                await mir.delete()
                await ctx.channel.send("Przegranko: Mirage " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(2)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=2")
                await mir.delete()
                await ctx.channel.send("Remis: Mirage " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def nuke(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=3")
    nke = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(nke) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=3")
    nke = await ctx.channel.send(
        "Dzisiaj Nuke " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + nke + " " + booba + " <:PeepoGlad:815276556863275028>")
    await nke.add_reaction("<:plus1:278220303639904257>")
    await nke.add_reaction("<:minus1:278220095447367681>")
    await nke.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=3")
                conn.commit()
                conn.close()
                await nke.delete()
                await ctx.channel.send("Wygranko: Nuke " + "<:proste:674360939134320640>")
                obliczanie_win_lose(3)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=3")
                conn.commit()
                conn.close()
                await nke.delete()
                await ctx.channel.send("Przegranko: Nuke " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(3)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=3")
                await nke.delete()
                await ctx.channel.send("Remis: Nuke " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def dust(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=4")
    dd = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(dd) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=4")
    dd = await ctx.channel.send(
        "Dzisiaj Mapa Majkela " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + dd + " " + booba + " <:PeepoGlad:815276556863275028>")
    await dd.add_reaction("<:plus1:278220303639904257>")
    await dd.add_reaction("<:minus1:278220095447367681>")
    await dd.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=4")
                conn.commit()
                conn.close()
                await dd.delete()
                await ctx.channel.send("Wygranko: Dust " + "<:proste:674360939134320640>")
                obliczanie_win_lose(4)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=4")
                conn.commit()
                conn.close()
                await dd.delete()
                await ctx.channel.send("Przegranko: Dust " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(4)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=4")
                await dd.delete()
                await ctx.channel.send("Remis: Dust " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def overpass(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=5")
    ovp = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(ovp) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=5")
    ovp = await ctx.channel.send(
        "Dzisiaj Overpass " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + ovp + " " + booba + " <:PeepoGlad:815276556863275028>")
    await ovp.add_reaction("<:plus1:278220303639904257>")
    await ovp.add_reaction("<:minus1:278220095447367681>")
    await ovp.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=5")
                conn.commit()
                conn.close()
                await ovp.delete()
                await ctx.channel.send("Wygranko: Overpass " + "<:proste:674360939134320640>")
                obliczanie_win_lose(5)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=5")
                conn.commit()
                conn.close()
                await ovp.delete()
                await ctx.channel.send("Przegranko: Overpass " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(5)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=5")
                await ovp.delete()
                await ctx.channel.send("Remis: Overpass " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def vertigo(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=6")
    vrt = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(vrt) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=6")
    vrt = await ctx.channel.send(
        "Dzisiaj Vertigo " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + vrt + " " + booba + " <:PeepoGlad:815276556863275028>")
    await vrt.add_reaction("<:plus1:278220303639904257>")
    await vrt.add_reaction("<:minus1:278220095447367681>")
    await vrt.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=6")
                conn.commit()
                conn.close()
                await vrt.delete()
                await ctx.channel.send("Wygranko: Vertigo " + "<:proste:674360939134320640>")
                obliczanie_win_lose(6)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=6")
                conn.commit()
                conn.close()
                await vrt.delete()
                await ctx.channel.send("Przegranko: Vertigo " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(6)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=6")
                await vrt.delete()
                await ctx.channel.send("Remis: Vertigo " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ancient(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=7")
    anc = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(anc) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=7")
    anc = await ctx.channel.send(
        "Dzisiaj Ancient " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + anc + " " + booba + " <:PeepoGlad:815276556863275028>")
    await anc.add_reaction("<:plus1:278220303639904257>")
    await anc.add_reaction("<:minus1:278220095447367681>")
    await anc.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=7")
                conn.commit()
                conn.close()
                await anc.delete()
                await ctx.channel.send("Wygranko: Ancient " + "<:proste:674360939134320640>")
                obliczanie_win_lose(7)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=7")
                conn.commit()
                conn.close()
                await anc.delete()
                await ctx.channel.send("Przegranko: Ancient " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(7)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=7")
                await anc.delete()
                await ctx.channel.send("Remis: Ancient " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def train(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=8")
    trn = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(trn) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=8")
    trn = await ctx.channel.send(
        "Dzisiaj Pociong " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + trn + " " + booba + " <:PeepoGlad:815276556863275028>")
    await trn.add_reaction("<:plus1:278220303639904257>")
    await trn.add_reaction("<:minus1:278220095447367681>")
    await trn.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=8")
                conn.commit()
                conn.close()
                await trn.delete()
                await ctx.channel.send("Wygranko: Train " + "<:proste:674360939134320640>")
                obliczanie_win_lose(8)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=8")
                conn.commit()
                conn.close()
                await trn.delete()
                await ctx.channel.send("Przegranko: Train " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(8)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=8")
                await trn.delete()
                await ctx.channel.send("Remis: Train " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cache(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=9")
    cch = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(cch) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=9")
    cch = await ctx.channel.send(
        "Dzisiaj Keszyk " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + cch + " " + booba + " <:PeepoGlad:815276556863275028>")
    await cch.add_reaction("<:plus1:278220303639904257>")
    await cch.add_reaction("<:minus1:278220095447367681>")
    await cch.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=9")
                conn.commit()
                conn.close()
                await cch.delete()
                await ctx.channel.send("Wygranko: Cache " + "<:proste:674360939134320640>")
                obliczanie_win_lose(9)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=9")
                conn.commit()
                conn.close()
                await cch.delete()
                await ctx.channel.send("Przegranko: Cache " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(9)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=9")
                await cch.delete()
                await ctx.channel.send("Remis: Cache " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def iris(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=10")
    ins = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(ins) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=10")
    ins = await ctx.channel.send(
        "Dzisiaj Iris " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + ins + " " + booba + " <:PeepoGlad:815276556863275028>")
    await ins.add_reaction("<:plus1:278220303639904257>")
    await ins.add_reaction("<:minus1:278220095447367681>")
    await ins.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=10")
                conn.commit()
                conn.close()
                await ins.delete()
                await ctx.channel.send("Wygranko: Iris " + "<:proste:674360939134320640>")
                obliczanie_win_lose(10)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=10")
                conn.commit()
                conn.close()
                await ins.delete()
                await ctx.channel.send("Przegranko: Iris " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(10)
                backup_bazy()
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=10")
                await ins.delete()
                await ctx.channel.send("Remis: Iris " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def office(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=11")
    off = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(off) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=11")
    off = await ctx.channel.send(
        "Dzisiaj Office " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + off + " " + booba + " <:PeepoGlad:815276556863275028>")
    await off.add_reaction("<:plus1:278220303639904257>")
    await off.add_reaction("<:minus1:278220095447367681>")
    await off.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=11")
                conn.commit()
                conn.close()
                await off.delete()
                await ctx.channel.send("Wygranko: Office " + "<:proste:674360939134320640>")
                obliczanie_win_lose(11)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=11")
                conn.commit()
                conn.close()
                await off.delete()
                await ctx.channel.send("Przegranko: Office " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(11)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=11")
                await off.delete()
                await ctx.channel.send("Remis: Office " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def agency(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=12")
    agc = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(agc) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=12")
    agc = await ctx.channel.send(
        "Dzisiaj Agencja " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + agc + " " + booba + " <:PeepoGlad:815276556863275028>")
    await agc.add_reaction("<:plus1:278220303639904257>")
    await agc.add_reaction("<:minus1:278220095447367681>")
    await agc.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=12")
                conn.commit()
                conn.close()
                await agc.delete()
                await ctx.channel.send("Wygranko: Agency " + "<:proste:674360939134320640>")
                obliczanie_win_lose(12)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=12")
                conn.commit()
                conn.close()
                await agc.delete()
                await ctx.channel.send("Przegranko: Agency " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(12)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=12")
                await agc.delete()
                await ctx.channel.send("Remis: Agency " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def inferno(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=13")
    inf = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(inf) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=13")
    inf = await ctx.channel.send(
        "Dzisiaj Inferno " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + inf + " " + booba + " <:PeepoGlad:815276556863275028>")
    await inf.add_reaction("<:plus1:278220303639904257>")
    await inf.add_reaction("<:minus1:278220095447367681>")
    await inf.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=13")
                conn.commit()
                conn.close()
                await inf.delete()
                await ctx.channel.send("Wygranko: Inferno " + "<:proste:674360939134320640>")
                obliczanie_win_lose(13)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=13")
                conn.commit()
                conn.close()
                await inf.delete()
                await ctx.channel.send("Przegranko: Inferno " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(13)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=13")
                await inf.delete()
                await ctx.channel.send("Remis: Inferno " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def climb(ctx):
    conn = sqlite3.connect("mapy.db", timeout=20)
    c = conn.cursor()
    c.execute("SELECT liczba FROM mapy WHERE id_mapy=14")
    grd = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "")
    if int(grd) == 1:
        booba = "raz"
    else:
        booba = "razy"
    c.execute("UPDATE mapy SET liczba=liczba+1 WHERE id_mapy=14")
    grd = await ctx.channel.send(
        "Dzisiaj Climb " + "<@&391947653618991106>" + " " + "<:pogchamp4:809889459944161290>"
        + ", mape gralismy: " + grd + " " + booba + " <:PeepoGlad:815276556863275028>")
    await grd.add_reaction("<:plus1:278220303639904257>")
    await grd.add_reaction("<:minus1:278220095447367681>")
    await grd.add_reaction("✏️")
    conn.commit()
    conn.close()
    backup_bazy()

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            conn = sqlite3.connect("mapy.db")
            c = conn.cursor()
            if str(reaction.emoji) == "<:plus1:278220303639904257>":
                c.execute("UPDATE mapy SET win=win+1 WHERE id_mapy=14")
                conn.commit()
                conn.close()
                await grd.delete()
                await ctx.channel.send("Wygranko: Climb " + "<:proste:674360939134320640>")
                obliczanie_win_lose(14)
                backup_bazy()
            if str(reaction.emoji) == "<:minus1:278220095447367681>":
                c.execute("UPDATE mapy SET lose=lose+1 WHERE id_mapy=14")
                conn.commit()
                conn.close()
                await grd.delete()
                await ctx.channel.send("Przegranko: Climb " + "<:Pepe:236556210508136458>")
                obliczanie_win_lose(14)
                backup_bazy()
            if str(reaction.emoji) == "✏️":
                c.execute("UPDATE mapy SET draw=draw+1 WHERE id_mapy=14")
                await grd.delete()
                await ctx.channel.send("Remis: Climb " + "<:Omegalul:428861885111205888>")
                conn.commit()
                conn.close()
                backup_bazy()




client.run(TOKEN)
