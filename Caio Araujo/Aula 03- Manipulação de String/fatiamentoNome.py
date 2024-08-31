nomeCompleto = 'Caio de Araujo Pereira'

primeiroNome = nomeCompleto[:4]
ultimoNome = nomeCompleto[-7:]
print(f'Meu primeiro nome é {primeiroNome}')
print(f' meu ultimo nome é {ultimoNome}')


qtdChar = len(nomeCompleto)
print(f'No nome temos {qtdChar} caracteres')


letra = 'o'
qtdLetrasO = nomeCompleto.count(letra)
print(f'No nome temos {qtdLetrasO} letras {letra}')


palavra = 'Pereira'
posicaoPalavra = nomeCompleto.find(palavra)
print(f'A palavra {palavra} inicia na posição {posicaoPalavra}')


nome1 = 'silva'
nome2 = 'souza'
nome3 = 'santos'

verificaPalavra = nome1 in nomeCompleto
print(f'A palavra {nome1} esta no texto ? {verificaPalavra}')

verificaPalavra = nome2 in nomeCompleto
print(f'A palavra {nome2} esta no texto ? {verificaPalavra}')

verificaPalavra = nome3 in nomeCompleto
print(f'A palavra {nome3} esta no texto ? {verificaPalavra}')