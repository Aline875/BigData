# -*- coding: utf-8 -*-
"""Exercício_Python_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fDPWSeIP2IYYkNJsCiEIetv9E4yKAq00

**Exercício 1 - Aquecimento de Python para Ciência de Dados**

1. Imprima "Hello, World!" no console.
"""

print ("Hello, World!")

"""2. Crie uma variável x com valor 10 e imprima seu valor."""

x = 10
print (x)

"""3. Some dois números e exiba o resultado."""

a = 3
b = 6
resultado = a + b
print (resultado)

"""4. Verifique se um número é par ou ímpar.

"""

num = 10
if num%2 == 0:
  print (f"{num} é par")
else:
  print (f"{num} é ímpar")

"""5. Crie uma função que receba dois números e retorne a soma deles."""

def soma(a, b):
  return a + b

resultado = soma(5,8)
print(resultado)

"""6. Crie uma lista com os números de 1 a 5 e imprima-a.

"""

lista_numeros = list(range(1, 6))
print(lista_numeros)

"""7. Adicione o número 6 à lista criada na questão anterior.

"""

lista_numeros.append(6)
print(lista_numeros)

"""8. Remova o número 3 da lista."""

lista_numeros.remove(3)
print(lista_numeros)

"""9. Acesse o terceiro elemento da lista."""

terceiro_numero = lista_numeros[2]
print(terceiro_numero)

"""10. Imprima o tamanho da lista."""

tamanho_lista = len(lista_numeros)
print(tamanho_lista)

"""11. Crie um dicionário com informações de um carro (marca, modelo, ano)."""

carro = {
    "marca": "Jeep",
    "modelo": "Renegade",
    "ano": 2022
}

print(carro)

"""12. Acesse o valor associado à chave "marca" no dicionário."""

marca_carro = carro["marca"]

print(marca_carro)

"""13. Adicione uma nova chave "cor" com valor "preto" ao dicionário."""

carro["cor"] = "preto"

print(carro)

"""14. Verifique se a chave "modelo" existe no dicionário.

"""

existe_modelo = "modelo" in carro

print(existe_modelo)

"""15. Itere sobre as chaves do dicionário e imprima cada uma delas."""

for chave in carro.keys():
    print(chave)

"""15. Itere sobre as chaves do dicionário e imprima cada uma delas."""

for chave in carro.keys():
    print(chave)

"""17. Crie uma função que receba uma lista e retorne a soma dos elementos."""

def soma_elementos(lista):
    return sum(lista)

numeros = [1, 2, 3, 4, 5]
resultado = soma_elementos(numeros)
print(resultado)

"""18. Crie uma função que receba um dicionário e retorne todas as suas chaves.

"""

def obter_chaves(dicionario):
    return dicionario.keys()

carro = {
    "marca": "Jeep",
    "modelo": "Renegade",
    "ano": 2022,
    "cor": "preto"
}

chaves_carro = obter_chaves(carro)
print(chaves_carro)

"""
19. Crie uma função que receba um dicionário e imprima chave e valor em linhas separadas."""

def imprimir_chaves_valores(dicionario):
    for chave, valor in dicionario.items():
        print(f"Chave: {chave}")
        print(f"Valor: {valor}")
        print()

carro = {
    "marca": "Jeep",
    "modelo": "Renegade",
    "ano": 2022,
    "cor": "preto"
}

imprimir_chaves_valores(carro)

"""20. Crie uma classe chamada Pessoa com atributos nome e idade, e um método que imprima esses dados."""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

pessoa1 = Pessoa("Aline Kessy", 26)
pessoa1.exibir_dados()