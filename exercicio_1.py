"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""
número_inteiro = int(input("Digite um número inteiro:"))

if número_inteiro % 2 == 0:
    print("Par")
    
else:
    print("Ímpar")
