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
    nascimento = 0
    func['nome']=input("Insira o nome")
    while nascimento < 1900:
        nascimento = int(input("insira o ano de nascimento"))
    func['idade'] = 2019 - nascimento
    func['CTPS'] = int(input("Insira a CTPS"))
    if func['CTPS'] != 0:
        func['anocontratação'] = int(input("Insira o ano de contratação"))
        func['salario'] = input("Insira o salário")
        func['aposentadoria'] = 35 - (2019 - func['anocontratação'])
        if func['aposentadoria'] <= 0:
            func['aposentadoria'] = 'Aposentado'
    print(f'O nome é {func["nome"]}. o Ano de nascimento é {func["idade"]}')
    print(f'CTPS tem valor de {func["CTPS"]}')
    if func['CTPS'] != 0:
        print(f'Contratação tem valor de: {func["anocontratação"]}')
        print(f"O salário tem valor de {func['salario']}. Aposentadoria tem valor de {func['aposentadoria']}")
