# Início das variáveis globais
lista_peca = []
codigo_peca = 0

# Início de cadastrarPeca()
def cadastrarPeca(codigo):
    print('Você selecionou a Opção de Cadastrar Peça')
    print('Código da Peça: {}'.format(codigo))
    nome = input('Por favor entre com o NOME da peça: ')
    fabricante = input('Por favor entre com o FABRICANTE da peça: ')
    valor = int(input('Por favor entre com o VALOR (R$) da peça: '))
    dicionarioPeca = {'codigo': codigo,
                      'nome': nome,
                      'fabricante': fabricante,
                      'valor': valor}
    lista_peca.append(dicionarioPeca.copy())
# Fim de cadastrarPeca()

# Início de consultarPeca()
def consultarPeca():
    global peca # Comando global
    print('Você selecionou a Opção de Consultar Peça')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n' +
                                '1 - Consultar todas as Peças\n' +
                                '2 - Consultar Peças por Código\n' +
                                '3 - Consultar Peças por Fabricante\n' +
                                '4 - Retornar\n' +
                                '>>')
        if opcao_consultar == '1':
            for peca in lista_peca:
                print('--------------------')
                for key, value in peca.items():
                 print('{}: {}'.format(key, value))
                print('--------------------')
        elif opcao_consultar == '2':
            codigo_peca = int(input('Digite o CÓDIGO da peça: '))
            for peca in lista_peca:
                if peca['codigo'] == codigo_peca:
                    print('--------------------')
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))
                    print('--------------------')
        elif opcao_consultar == '3':
            fabricante_peca = input('Digite o FABRICANTE da peça: ')
            for peca in lista_peca:
                if peca['fabricante'] == fabricante_peca:
                    print('--------------------')
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))
                    print('--------------------')
        elif opcao_consultar == '4':
            return  # Sair da função consultar e volta para o programa principal
        else:
            print('Opção inválida! Tente novamente!')  # Caso o usuário digite uma opção inexistente
            continue
# Fim de consultarPeca()

# Início de removerPeca()
def removerPeca():
    print('Você selecionou a Opção de Remover Peça')
    codigo_peca = int(input('Digite o CÓDIGO da peça a ser removida: '))
    for peca in lista_peca:
        if peca['codigo'] == codigo_peca:
            lista_peca.remove(peca)
# Fim de removerPeca()

# Programa principal
print('Bem Vindo ao Controle de Estoque da Bicicletaria da Sheila Hui Yi Chiu RU:4412400')
while True: # Laço inicial do programa
    opcao_principal = input('Escolha a opção desejada:\n' +
                            '1 - Cadastrar Peças\n' +
                            '2 - Consultar Peças\n' +
                            '3 - Remover Peças\n' +
                            '4 - Sair\n' +
                            '>>')
    if opcao_principal == '1':
        codigo_peca = codigo_peca + 1
        cadastrarPeca(codigo_peca)
    elif opcao_principal == '2':
        consultarPeca()
    elif opcao_principal == '3':
        removerPeca()
    elif opcao_principal == '4':
        break
    else:
        print('Opção inválida! Tente novamente!') # Caso o usuário digite uma opção inexistente
        continue
# Fim do programa principal
