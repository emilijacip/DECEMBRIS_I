"""
Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.
Izmantojiet GIT, lai izsekotu izmaiņas programmas kodā un izveidotu komitus, tos noevoetojot arī GITHUB.
"""
skaitlis=int(input("Ievadiet skaitli: "))
if skaitlis < 1:
        print("Ievadiet pozitīvu skaitli.")
else:
    for skaitlis1 in range(1,skaitlis+1):
           print (skaitlis1)