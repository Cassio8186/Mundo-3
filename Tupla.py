def desafio72():
    x = int(input("Insira o numero de 0 a 20"))
    while x < 0 and x > 20:
        print("Insira o numero de 0 a 20")
    numero = (
    'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
    'Quatorze', 'Quinze', 'Desesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
    print(f"O numero que você digitou é: {numero[x]}")
def desafio73():
    times = (
    'Palmeiras', 'Corintias', 'Internacional', 'Cruzeiro', 'Santos', 'Grêmio', 'Atlético', 'Fluminense', 'Botafogo',
    'Flamengo')
    print(times[0:6])
    print(times[-4:])
    print(sorted(times))
    print(int(times.index('Internacional')) + 1)
def desafio74():
    import random
    a = (random.randint(0, 100000), random.randint(0, 100000), random.randint(0, 100000), random.randint(0, 100000),
         random.randint(0, 100000))
    print(a)
    print(sorted(a))
    print(sorted(a)[0], sorted(a)[4])
def desafio75():
    x1 = input("Digite um numero")
    x2 = input("Digite um numero")
    x3 = input("Digite um numero")
    x4 = input("Digite um numero")
    tupa = (x1 + x2 + x3 + x4)
    print(tupa)
    print(f"O valor 9 apareceu {tupa.count('9')} vezes")
    c = 0
    for x in tupa:
        if int(x) == 3:
            c += 1
    if c == 0:
        print("O valor 3 não foi digitado em nenhuma posição")
    else:
        print("O valor 3 apareceu na {} posição".format(tupa.index('3') + 1))
    c = 0
    for x in tupa:
        if int(x) % 2 == 0:
            c += 1
    print(f"Os numeros pares digitados foram {c}")
def desafio76():
    listagem=('casa', 1.0, 'tempero', 3.0, 'shampoo', 5.0,'condicionador', 8.1, 'perfume', 10.0)
    print("{}".format("="*27).center(5))
    print(f'{"Listagem":=^27}')
    for pos in range(0,len(listagem)):
        if pos%2==0:
            print(f'{listagem[pos]:.<20}',end='')
        if pos%2==1:
            print(f'{listagem[pos]:.>7.2f}')
    print("{:=^27}".format(""))
def desafio77():
    lista=('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
    for c in lista:
        print(f"\nTemos na palavra {c}:",end=' ')
        for letra in c:
            if letra.lower() in 'aeiou':
                print(letra,end=' ')
