import sqlite3


def obliczanie_win_lose(id_mpy):
    conn = sqlite3.connect("mapy.db")
    c = conn.cursor()
    c.execute("SELECT win FROM mapy WHERE id_mapy=?", (id_mpy,))
    w = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")

    c.execute("SELECT lose FROM mapy WHERE id_mapy=?", (id_mpy,))
    l = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")

    c.execute("SELECT liczba FROM mapy WHERE id_mapy=?", (id_mpy,))
    liczba_gier = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")



    w_l = (int(w)/int(liczba_gier)) * 100
    w_l_g = int(w_l)
    c.execute("UPDATE mapy SET win_lose=? WHERE id_mapy=?", [w_l_g, id_mpy])
    conn.commit()
    conn.close()

def obliczanie_stare_win_lose(id_mpy):
    conn = sqlite3.connect("mapy.db")
    c = conn.cursor()
    c.execute("SELECT win_starej FROM stare_mapy WHERE id_starej=?", (id_mpy,))
    w = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")

    c.execute("SELECT lose_starej FROM stare_mapy WHERE id_starej=?", (id_mpy,))
    l = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")

    c.execute("SELECT liczba_starej FROM stare_mapy WHERE id_starej=?", (id_mpy,))
    liczba_gier = str(c.fetchone()).replace("(", "").replace(",", "").replace(")", "").replace("'", "")



    w_l = (int(w)/int(liczba_gier)) * 100
    w_l_g = int(w_l)
    c.execute("UPDATE stare_mapy SET win_lose_starej=? WHERE id_starej=?", [w_l_g, id_mpy])
    conn.commit()
    conn.close()
