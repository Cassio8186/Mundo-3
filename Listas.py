import random
def desafio78():
    num=[]
    for c in range (5):
        num.append(input("Insira um numero"))
    sor=num[:]
    sor.sort()
    min=sor[0]
    max=sor[len(sor)-1]
    print(f"Você digitou os valores {num}")
    print(f"O maior valor digitado foi {max} nas posições",end=' ')
    for pos, val in enumerate(num):
        if max in num[pos]:
            print(f"{pos+1}", end='.. ')
    print(f"\nO menor valor digitado foi {min} nas posições",end=' ')
    for pos, val in enumerate(num):
        if min in num[pos]:
            print(f"{pos+1}", end='.. ')
import os
from time import sleep
# clear = '\n'*100
# XO{a11=0, a12=0, a13=0, a21=0, a22=0, a23=0, a31=0, a32=0, a33=0}
# print('{}'.format('-'*20))
# print('{:>8}{}{:^1}{}{:^1}'.format(a11,'│',a12,'│',a13))
# print('{:>8}{}{:^1}{}{:^1}'.format(a21,'│',a22,'│',a23))
# print('{:>8}{}{:^1}{}{:^1}'.format(a31,'│',a32,'│',a33))
# print('{}'.format('-'*20))
def desafio79():
    lista=[]
    d='1'
    while d=='1':
        x=int(input("Insira um numero na lista, digite [S/N]"))
        if x not in lista:
            lista.append(x)
        d=input("Deseja continuar?")
        if d[0].lower().strip()=='s':
            d='1'
        if d[0].lower().strip()=='n':
            d='0'
    lista.sort()
    print(lista)
def desafio80():
    lista=[]
    for c in range(5):
        x=int(input("Insira o numero na lista"))
        for pos, val in enumerate(lista):
            if x < val:
                lista.insert(pos, x)
                print(f"Na posição {pos+1} foi inserido o valor {x}\n")
                break
        else:
            lista.append(x)
            print("Adicionado ao final da lista\n")
        print(lista)
def desafio81():
    lista=[]
    c=0
    while True:
        lista.append(int(input("Insira valores")))
        c+=1
        print(c,lista)
        d=input("Deseja continuar?")
        if d[0].strip().lower()!='s':
            break
    print(f"Foram digitados {c} numeros, a lista decrescente é: ")
    lista.sort(reverse=True)
    print(lista)
    if 5 in lista:
        print("5 Consta na lista")
    else:
        print("Não possui 5 na lista")
def desafio82():
    lista = []
    pares = []
    impares = []
    while True:
        lista.append(int(input("Insira valores\n")))
        d = input("Deseja continuar?")
        if d[0].strip().lower() != 's':
            break
    for pos, val in enumerate(lista):
        if val % 2 == 0:
            pares.append(lista[pos])
        else:
            impares.append(lista[pos])
    print(f"lista completa: {lista}")
    if len(pares) == 0:
        print("Não há pares")
    else:
        print(f'pares: {pares}')
    if len(impares) == 0:
        print("Não há impares")
    else:
        print(f'pares: {impares}')
def desafio83():
    exp=list()
    expr=list()
    exp.append(str(input("Insira uma expressão\n")))
    for c in exp:
        for val in c:
            if val == '(':
                expr.append(')')
            elif val == ')':
                expr.append('(')
    c=0
    for pos,val in enumerate(expr):
        if val == ')':
            posicao=pos+1
            c+=1
            for vall in range(posicao,len(expr)):
                if expr[vall]=='(':
                    c-=1
                    if c==0:
                        break
                else:
                    c+=1
    if c!=0:
        print("A expressão é inválida")
    else:
        print("A expressão é válida")
def praticalista2():
    lista=[['Maria',1],['Marcio',2],['Cassio',3]]
    for c in range (0,len(lista)):
        print(lista[c])
    for b in range(0,len(lista[c])):
        print('b',lista[c][b])
def desafio84():
    pessoa=list()
    lista=list()
    gordos=list()
    magros=list()
    maior = 0
    menor = 999999
    maio = []
    meno = []
    con=0
    while True:
        pessoa.append(str(input("Qual seu nome?")))
        pessoa.append(float(input("Qual seu peso?")))
        c=input("Deseja continuar? [S/N])")
        print(c[0].strip().lower())
        lista.append(pessoa[:])
        pessoa.clear()
        con+=1
        if c[0].strip().lower()=='n':
            break
    for p in range(0,len(lista)):
        if float(lista[p][1]) > maior:
            maior = float(lista[p][1])
        if float(lista[p][1]) < menor:
            menor = float(lista[p][1])
    for p in range(0,len(lista)):
        if lista[p][1]==maior:
            maio.append(lista[p][0])
        if lista[p][1]==menor:
            meno.append(lista[p][0])
    print(f'O total de pessoas inseridas foi {con}')
    print(f'O maior peso foi {maior}kg. peso de:{maio}')
    print(f'O menor peso foi {menor}kg. peso de:{meno}')
def desafio85():
    numb=list()
    par=0
    impar=0
    for c in range(7):
        x=int(input("Insira o numero"))
        if x%2 == 0 and par == 0:
            numb.insert(0,[x])
            par+=1
        elif x % 2 == 0 and par > 0:
            numb[0].append(x)
            par += 1
        if x%2 != 0 and impar == 0:
            numb.insert(1,[x])
            impar+=1
        elif x%2 != 0 and impar > 0:
            numb[1].append(x)
            impar+=1

        print(numb)

    numb[0].sort()
    numb[1].sort()
    print(f'Ao todo {par+impar} numeros foram inseridos')
    print(f'Os números pares são: {numb[0]} e os numeros impares são: {numb[1]}')
def desafio86():
    num=list()
    x=0
    pares=0
    tercoluna=0
    segundalinha=0
    for c in range(3):
        for b in range(3):
            x=int(input(f'Insira o numero na posição[{c},{b}]:'))
            if b==0:
                num.insert(c,[x])
            else:
                num[c].append(x)
    for c in range(3):
        for b in range(3):
            if b!=2:
                print(f'[ {num[c][b]} ]', end='')
            else:
                print(f'[ {num[c][b]} ]', end='\n')
            if num[c][b]%2==0:
                pares+=num[c][b]
            if c==1:
                if num[c][b]>segundalinha:
                    segundalinha=num[c][b]
            if b==2:
                tercoluna+=num[c][b]
    print(f'A soma dos valores pares é: {pares}')
    print(f'A soma dos terceiros valores da terceira coluna: {tercoluna}')
    print(f'O maior valor da segunda linha é: {segundalinha}')
def desafio87():
    from time import sleep
    num=list()
    x=int(input("Quantos jogos você quer sortear?"))
    print('-='*3,f'Sorteando {x} jogos','-='*3)
    for c in range(x):
        for b in range(6):
            while True:
                s = 0
                al = random.randint(0, 60)
                for d in range(0,len(num)):
                    if num[d]==al:
                        s+=1
                if s==0:
                    break
            if b==0:
                num.insert(c,[al])
            else:
                num[c].append(al)
            num[c].sort()
    for c in range(len(num)):
        sleep(1)
        print(num[c])
    print('-='*3,f' < Boa sorte! > ','-='*3+'-')
def desafio88():
    lg=[['cassio',[5.0,2.5],3.75],['alanna',[7.0,9.0],8.0],['illeana',[4.0,5.0],4.5]]
    for c in range(0,len(lg)):
        for b in range(0,len(lg[c])):
            if b==1:
                for a in range(0,len(lg[c][b])):
                    print(c,b,a,lg[c][b][a])
            else:
                print(c, b, lg[c][b])
desafio88()

