#Atividade01

n1 = int(input('digite um valor: '))
n2 = int(input('digite um valor: '))
soma = n1 + n2 
print(f'A soma de {n1} + {n2} é igual a {soma}: ')



#Atividade 02

numeroBase = int(input('Digite um valor entre 1 a 10: '))
sucessor = numeroBase + 1
antecessor = numeroBase - 1
print(f'o numero antecessor é {antecessor} e o sucessor é {sucessor}')

#Atividade 03

import math

numeroPrime = int(input('Digite um numero entre 1 a 10: '))
dobro = numeroPrime + numeroPrime 
triplo = numeroPrime + numeroPrime + numeroPrime
quadrado = numeroPrime + numeroPrime + numeroPrime + numeroPrime
raiz = math.sqrt(numeroPrime)
print(f'o dobro é {dobro} \n o triplo é {triplo} \n o quadrado é {quadrado} \n e a raiz é {raiz}')

#Atividade 04

nota01 = int(input('digite sua primeira nota: '))
nota02 = int(input('digite sua segunda nota: '))
media = nota01 + nota02 
final = media / 2
print(f'Sua media é {final}')

#Atividade 05

carteiraReal = int(input('coloque seu valor em reais: '))
dolar = 5
divisao = carteiraReal / dolar
print(f'sua carteira em dolar é ${divisao}')

#Atividade Extra 01

numeroBase = int(input('digite um valor entre 1 a 10: '))
numeroExpoente = numeroBase * numeroBase
print(f'O quadrado desse numero é {numeroExpoente}')

#Atividade Extra 02

caractere1 = str(input('digite um caractere: '))
caracter2 = str(input('digite outro caractere: '))
print(f'O usuario digitou {caractere1} e {caracter2}')

#Atividade Extra 03

numero01 = int(input('Digite um valor entre 1 a 10: '))
sucessor01 = numero01 + 1
antecessor01 = numero01 - 1
print(f'o numero antecessor é {antecessor01} e o sucessor é {sucessor01}')

#Atividade Extra 04

base = int(input('digite a base: '))
altura = int(input('digite a altura: '))
perimetro = (base * 2) + (altura * 2)
area = base * altura 
print(f'o perimetro do retangulo é igual a {perimetro} e a area é igual a {area}: ')

#Atividade Extra 05

valorPrestacao = int(input('Digite o valor da prestação: '))
taxa = int(input('Digite o valor da taxa de juros anual em porcentagem: '))
tempo = int(input('Digite os dias de atraso: '))
prestacaoAtraso = valorPrestacao + (valorPrestacao * ((taxa/100)/365) * tempo)
print(f'O valor da prestação em atraso é de {prestacaoAtraso}: ')