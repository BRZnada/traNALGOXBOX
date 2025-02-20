import json
import os

print('Bem-vindo ao cadastro da Xbox!!')

def ler_valor_nao_vazio(nome_variavel):
    valor_lido = input(f'Digite o/a {nome_variavel}: ')
    while valor_lido == '': 
        print(f'{nome_variavel} não pode ficar vazio!')
        valor_lido = input(f'Digite o/a {nome_variavel}: ')
    return valor_lido

def confirmaSenha():
    senha = input('Digite sua senha: ')
    while senha == '':
        print('Senha não pode ser vazia!')
        senha = input('Digite sua senha: ')
    while len(senha) < 8:
        print("A senha tem que ter no mínimo 8 caracteres!")
        senha = input('Digite sua senha: ')
    confirmacaoSenha = input('Confirme sua senha: ')
    while confirmacaoSenha != senha:
        print("As senhas não coincidem!")
        confirmacaoSenha = input('Confirme sua senha: ')
    return senha

def lerPlataforma():
    plataforma_lida = input('Digite a plataforma (PC ou Xbox): ').lower()
    while plataforma_lida not in ['pc', 'xbox']:
        print('Digite uma plataforma válida (PC ou Xbox)!')
        plataforma_lida = input('Digite a plataforma: ').lower()
    return plataforma_lida

def cadastroXbox():
    nome = ler_valor_nao_vazio('nome')
    plataforma = lerPlataforma()
    senha = confirmaSenha()
    email = ler_valor_nao_vazio('email')
    return {'nome': nome, 'plataforma': plataforma, 'senha': senha, 'email': email}

def imprimir_cadastro():
    dados = lerjson()
    if not dados:
        print("\nNenhum cadastro encontrado!\n")
        return
    print("\nCadastros:")
    for i, cadastro in enumerate(dados, 1):
        print(f"\nCadastro {i}:")
        print(f"Nome:\t\t{cadastro['nome']}")
        print(f"Plataforma:\t{cadastro['plataforma']}")
        print(f"Email:\t\t{cadastro['email']}")
        print(f"Senha:\t\t{cadastro['senha']}")
    print("\n")
    
def lerjson():
    with open('cadastros.json', 'r') as arquivo:
        registros = json.load(arquivo)
        return registros

def salvarjson(registro):
    dados = json.dumps(registro, indent=2)
    with open('cadastros.json','w') as arquivo:
        arquivo.write(dados)
    

def excluir():
    dados = lerjson()
    if not dados:
        print("\nNenhum cadastro encontrado para excluir!\n")
        return
    print("\nCadastros disponíveis para exclusão:")
    for i, item in enumerate(dados, 1):
        print(f"{i}. {item['nome']} - {item['email']}")
    try:
        index = int(input("\nDigite o número do cadastro a excluir: ")) - 1
        if 0 <= index < len(dados):
            excluido = dados.pop(index)
            salvarjson(dados)
            print(f"\nCadastro '{excluido['nome']}' removido com sucesso.\n")
        else:
            print("\nNúmero inválido.\n")
    except ValueError:
        print("\nEntrada inválida.\n")

def editar():
    dados = lerjson()
    if not dados:
        print("\nNenhum cadastro encontrado para editar!\n")
        return
    print("\nCadastros disponíveis para edição:")
    for i, item in enumerate(dados, 1):
        print(f"{i}. {item['nome']} - {item['email']}")
    try:
        index = int(input("\nDigite o número do cadastro que deseja editar: ")) - 1
        if 0 <= index < len(dados):
            print("\nDeixe em branco se não quiser alterar um campo.")
            novo_nome = input("Novo nome: ") or dados[index]['nome']
            nova_plataforma = input("Nova plataforma (PC/Xbox): ").lower() or dados[index]['plataforma']
            while nova_plataforma not in ['pc', 'xbox']:
                print("Plataforma inválida! Digite 'PC' ou 'Xbox'.")
                nova_plataforma = input("Nova plataforma (PC/Xbox): ").lower() or dados[index]['plataforma']
            novo_email = input("Novo e-mail: ") or dados[index]['email']
            alterar_senha = input("Deseja alterar a senha? (S/N): ").strip().lower()
            nova_senha = confirmaSenha() if alterar_senha == 's' else dados[index]['senha']
            dados[index] = {'nome': novo_nome, 'plataforma': nova_plataforma, 'email': novo_email, 'senha': nova_senha}
            salvarjson(dados)
            print("\nCadastro atualizado com sucesso!\n")
        else:
            print("\nNúmero inválido.\n")
    except ValueError:
        print("\nEntrada inválida.\n")

while True:
    print("\n1. Criar cadastro \n2. Imprimir cadastros \n3. Excluir um cadastro \n4. Editar um cadastro \n5. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        novo_cadastro = cadastroXbox()
        cadastros = lerjson()
        cadastros.append(novo_cadastro)
        salvarjson(cadastros)
        print("\nCadastro salvo com sucesso!\n")
    elif opcao == "2":
        imprimir_cadastro()
    elif opcao == "3":
        excluir()
    elif opcao == "4":
        editar()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")