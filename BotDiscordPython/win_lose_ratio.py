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

    if int(w) == 0:
        c.execute("UPDATE mapy SET win_lose=0 WHERE id_mapy=?", (id_mpy,))
        conn.commit()
        conn.close()
    elif int(l) == 0:
        c.execute("UPDATE mapy SET win_lose=100 WHERE id_mapy=?", (id_mpy,))
        conn.commit()
        conn.close()
    else:
        if ((int(w)/int(liczba_gier)) * 100) > 100:
            c.execute("UPDATE mapy SET win_lose=100 WHERE id_mapy=?", (id_mpy,))
            conn.commit()
            conn.close()
        else:
            w_l = (int(w)/int(liczba_gier)) * 100
            w_l_g = int(w_l)
            c.execute("UPDATE mapy SET win_lose=? WHERE id_mapy=?", [w_l_g, id_mpy])
            conn.commit()
            conn.close()