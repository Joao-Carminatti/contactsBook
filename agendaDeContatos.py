print("Esse programa simulará uma agenda de contatos!")

contatos = {}

def adicionarContato(contatos):
    nomeContato = str(input("Digite o nome do contato: "))
    numeroContato = int(input("Digite o número do contato (sem sinal): "))
    contatos.update({nomeContato: numeroContato})
    print(contatos)

def removerContato(contatos):
    nomeContato = str(input("Digite o nome do contato que deseja remover: "))
    del contatos[nomeContato]
    print(contatos)

def pesquisarContato(contatos):
    nomeContato = str(input("Digite o nome do contato que desejas pesquisar: "))
    if nomeContato in contatos:
        print("Contato está na lista!")
    else:
        print("Contato não encontrado!")

def sair():
    return "Você está saindo do programa!"

while len(contatos) < 4:

    print("Opções:\n1. Adicionar Contato\n2. Remover contato\n3. Pesquisar Contato\n4. Sair")
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print(adicionarContato(contatos))
        case 2:
            print(removerContato(contatos))
        case 3:
            print(pesquisarContato(contatos))
        case 4:
            print(sair())
            break
        case other:
            print("Você não digitou uma opção válida!")
    