def pratica():
    lista=dict()
    lista['nome']=input("Insira nome")
    lista['media']=float(input("insira a média"))
    print(f'A média de {lista["nome"]} é {lista["media"]}', end=' ')
    if lista['media']>=7:
        print("e sua situação é aprovado")
    else:
        print("e sua situação é reprovada")
def desafio92():
    func=dict()
    func['nome']=input("Insira o nome")
    func['nasci']=input("insira o ano de nascimento")
    func['']