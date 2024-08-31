#Exercicio 01
nome = str(input("DIgite seu nome: "))

maiusculo = nome.upper()
minisculo = nome.lower()
print(f' Seu nome maiúsculo é {maiusculo} seu nome minúsculo é {minisculo}')
primeiro_nome = nome.split()[0]
nomeSem = nome.replace(' ', '')
print(len(nomeSem))
primeiro_nome = nome.split()[0]
print(len(primeiro_nome))

#Exercicio 02
cidade = str(input("Digite o nome de uma cidade: "))
cidade1 = cidade.split()[0]
print("Santos" in cidade1)  

#Exercicio 03
nome = str(input("Digite seu nome: "))
print("Silva" in nome)

#Exercicio 04
texto = str(input('Digite sua frase:'))

qntA = texto.count("a")
print(f"No texto tem {qntA} letras A")

posição_ini = ("a")
posição1 = texto.find(posição_ini)
print(f"{posição_ini} inicia na {posição1} posição")

ult_posição = ("a")
posição2 = texto.rfind(ult_posição)
print(f"Ultima posição de A é {posição2}")

#Desafio 05
nome = str(input('Digite seu nome:'))
primeiroNome = nome.split()[0]
ultimoNome = nome.split()[-1]
print(f'Seu primeiro nome é {primeiroNome}')
print(f'Seu ultimo nome é {ultimoNome}')