texto = "Curso de Python"

setimaPosicao = texto[6]
print(setimaPosicao)

textoCurso = texto[:5]
print(textoCurso)

textoPython = texto[9:]
print(textoPython)

#Contar número de caracteres dentro do texto
qtdChar = len(texto)
print(f'Na frase temos {qtdChar} caracteres')

#Contar um número específico de letras dentro do texto
letra = 'o'
qtdLetrasO = texto.count(letra)
print(f'Na frase temos {qtdLetrasO} letras {letra}')

#Indentifica a posição onde inicia uma palavra 
palavra = 'Python'
posicaoPalavra = texto.find(palavra)
print(f'A palavra {palavra} inicia na posição {posicaoPalavra}')

#Identifica se existe a palavrano texto
verificaPalavra = palavra in texto 
print(f'A palavra {palavra} esta no texto ? {verificaPalavra}')

