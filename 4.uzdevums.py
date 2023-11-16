"""
Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.
"""
skaitlis=int(input("Ievadiet skaitli: "))
faktorials=1
for i in range(1, skaitlis +1):
    faktorials*=i 
print (f"Faktoriāls no {skaitlis} ir {faktorials}.")