from shutil import copy2

def backup_bazy():
    copy2("mapy.db", "mapy-backup.db")
