"""
#### Exercício 2 - Conversor de moeda

Você é uma casa de câmbio, recebe dinheiro em reais e transforma na moeda da viagem do usuário.

Você tem em caixa dólares, pesos argentinos e ienes.

Pergunte para o usuário para onde ele vai viajar:

Se ele falar "Estados Unidos", "Argentina" ou "Japão", faça o seguinte processo:
    Pergunte quantos reais ele vai converter. Receba o valor em float.
    Converta o valor para a moeda do país.
    Responda com o valor da moeda e em seguida o tipo da moeda (USD, ARS, ou JPY).

Se ele falar qualquer outra coisa, responda "Não temos essa moeda em caixa.".

Utilize as seguintes conversões:
5 reais = 1 USD
1 real = 180 ARS
1 real = 30 JPY

Obs:
Nos testes, vou tentar ignorar caso haja apenas uma diferença no número de casas decimais nas respostas.
Porém, se você quiser garantir que você imprima com exatamente 2 casas decimais você pode usar a seguinte sintaxe: f"{sua_variavel:.2f}".

Exemplo:
valor_em_dolares = 23.333333
print(f"{valor_em_dolares:.2f} USD")
>>> 23.33 USD

Mais informações sobre formatação de strings: https://realpython.com/python-f-strings/#interpolating-values-and-objects-in-f-strings

-------------------------------------------
Exemplos:

Qual país você vai viajar? Estados Unidos
Quantos reais você quer converter? 100

Resposta:
20.00 USD

-------------------------------------------
Qual país você vai viajar? Argentina
Quantos reais você quer converter? 100

Resposta:
18000.00 ARS

-------------------------------------------
Qual país você vai viajar? China

destino = input("Para onde irá viajar? ")

if destino == "Estados Unidos":
    moeda_real = float(input("Quanto irá converter? "))
    usd = moeda_real / 5
    print(f"{usd:.2f} USD")
    
elif destino == "Argentina":
    moeda_real = float(input("Quanto irá converter? "))
    ars = moeda_real * 180
    print(f"{ars:.2f} ARS")

elif destino == "Japão":
    moeda_real = float(input("Quanto irá converter? "))
    jpy = moeda_real * 30
    print(f"{jpy:.2f} JPY")

else:
    print("Não temos essa moeda em caixa")

Resposta:
Não temos essa moeda em caixa.
"""

destino = input("Para onde irá viajar? ")

if destino == "Estados Unidos":
    moeda_real = float(input("Quanto irá converter? "))
    usd = moeda_real / 5
    print(f"{usd:.2f} USD")
    
elif destino == "Argentina":
    moeda_real = float(input("Quanto irá converter? "))
    ars = moeda_real * 180
    print(f"{ars:.2f} ARS")

elif destino == "Japão":
    moeda_real = float(input("Quanto irá converter? "))
    jpy = moeda_real * 30
    print(f"{jpy:.2f} JPY")

else:
    print("Não temos essa moeda em caixa")
