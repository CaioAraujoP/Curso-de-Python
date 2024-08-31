#Trocando uma palavra dentro de um texto
texto = 'Caio Araujo'
trocaTexto = texto.replace('Araujo' , 'Pereira')
print(trocaTexto)

#Deixando todos os caracteres em maiúsculo
texto = 'CaIoArAujO@gmail.Com'
textoMaiusculo = texto.upper()
print(textoMaiusculo)

#Deixando todos os caracteres em minúsculo
textoMinusculo = texto.lower()
print(textoMinusculo)

#Deixando a primeira letra de cada palavra em Maiúsculo 
texto = 'meu primeiro curso no senai'
textoTitle = texto.title()
print(textoTitle)

#Deixando a primeira letra do texto em Maiúsculo 
textoCap = texto.capitalize() 
print(textoCap)

#Elimina espaços inuteis
texto = '      SENAI  '
print(f'A palavra {texto} tem {len(texto)} caracteres' )

textoStrip = texto.strip()
print(f'A palavra{textoStrip} tem {len(textoStrip)} caracteres')