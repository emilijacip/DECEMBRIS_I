"""
Izveidojiet Python programmu, kas atkarībā no pašreizējās stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu. (labrīt, labdien, labvakar)
"""
import datetime
laiks=datetime.datetime.now().hour
if 6<=laiks<12:
    print("Labrīt!")
elif 12<=laiks<18:
    print("Labdien!")
else:
    print("Labvakar!")