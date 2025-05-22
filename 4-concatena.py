 # Utilizando o concatenar

name = input("Digite o nome do filme: ")
yearLaunch = int(input("Digite o ano do filme: "))
noteMovie = float(input("Nota do filme: ")) 
planIncluded = input("Incluso no plano: ")
print("Nome: ",name)
print("Ano: ",yearLaunch)
print("Nota: ",noteMovie,"   -  ","Incluso no plano: ",planIncluded)

print(f"Nome: {name}\n"
      f"Ano: {yearLaunch}\n"
      )
