"""
Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.
"""
skaitlis=int(input("Ievadiet skaitli: "))
if skaitlis %2!=0:
    print(f"{skaitlis} ir nepāra skaitlis.")

else:
    print(f"{skaitlis} ir pāra skaitlis.")