# O return:é usada para retornar um valor de uma função. Quando uma função é chamada, ela executa um bloco de código e, em seguida, retorna um valor
import os
# Função para limpar a tela
def clean():
    os.system("cls")

# Função para pegar a opção do menu
def pegar_opcao():
    return input("Digite a opção desejada: ")

def inserir(usuarios):
    # ATENÇÃO: Todas as linhas abaixo DEVEM ter um TAB (4 espaços) de recuo
    user_name = input("Digite o nome do usuario: ").upper().strip()
    nome = input("Digite o seu nome: ").upper().strip()
    nascimento = input("Digite a data de nascimento: ")
    usuario_id = input("Digite seu ID único: ").upper().strip()

    # O dicionário TEM que estar aqui dentro para reconhecer 'user_name', 'nome', etc.
    dados_pessoa = {
        "Nome de usuario": user_name,
        "Nome": nome,
        "Nascimento": nascimento
    }

    # Esta linha também deve estar recuada (dentro do def)
    usuarios[usuario_id] = dados_pessoa
    
    print(f"\nUsuário {user_name} salvo com sucesso!")

    salvar(usuarios)

def salvar(usuarios):
    with open("usuarios.txt", "a") as site:
        for chave, dados in usuarios.items():
            site.write(chave + ":" + str(dados))




def pesquisar(usuarios):
    chave = input("Digite o ID do usuario que deseja pesquisar: ")

    if chave in usuarios:

        print(f"\nUsuário encontrado!")
        print(f"Nome: {usuarios[chave]['Nome']}")
        print(f"Nascimento: {usuarios[chave]['Nascimento']}")
        print(f"User: {usuarios[chave]['Nome de usuario']}")

    else:

        print(f"\nErro: Usuário '{chave}' não encontrado.")


def excluir(usuarios):
    chave = input("Digite o ID do usuario que deseja excluir: ")

    if chave in usuarios:
        del usuarios[chave]
        print(f"\nUsuário excluido com sucesso!")
    else:
        print(f"\nErro: Usuário '{chave}' nao encontrado.")


def listar(usuarios):
    if not usuarios:
        print("\nNenhum usuário cadastrado.")

    else:
        print("\n--LISTA DE USUARIOS--")
        for chave, dados in usuarios.items():
            print(f"ID: {chave} | Nome: {dados['Nome']}")

def sair():
    print("ENCERRANDO O SISTEMA...")
    exit()



