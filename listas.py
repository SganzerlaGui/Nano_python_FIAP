from arquivo import *
#usuarios = {}

#print(usuarios)

#usuarios = {
#        "Guilherme" : ["Guilherme Sganzerla", "20/03/2026", "Programador"],
#        "Tatiany" : ["Tatiany Sganzerla", "20/03/2026", "Fisioterapeuta"]
#}

#print(usuarios)

#usuarios ["Florinda"] = ["Florinda da Silva", "09/04/2025", "Juiza"] 

#print(usuarios)


#usuarios = {}

#opcao = perguntar()
#while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L" or opcao == "S":    
#    if opcao == "I":
#        inserir(usuarios)
#        #----- Este é um exemplo de código que utiliza um dicionário para armazenar informações de usuários.
#        # ------O dicionário 'usuarios' é usado para armazenar as informações de cada usuário, onde a chave é o nome do usuário e o valor é uma lista contendo o nome completo, a data de nascimento e a função do usuário.
#        # -------A função 'inserir' é responsável por adicionar um novo usuário ao dicionário 'usuarios', solicitando ao usuário as informações necessárias.
#        # -------O código também permite a visualização das informações de cada usuário, a remoção de um usuário específico e a impressão das informações de todos os usuários.
#        # --------O arquivo 'arquivo.py' contém a implementação das funções 'inserir', 'remover' e 'imprimir', enquanto o arquivo 'listas.py' contém o código principal que interage com o usuário.    
#    opcao = perguntar()

#---Lista = []
#---dicionnario {}
#---tupla()    


usuarios = {}

emails = ["Gsc@gmail.com", "01oi@gmail.com"]

tupla = list(enumerate(emails))

#------Tupla para retornar mais de 1 valor de 1 metodo
#--------enumerate vai voltar enumerado: 11,2,3,4,5,6,7......
#l-------ist concatena a numeração e os gmails em uma tupla

for chave in range(0, len(tupla)):
    
    print(f"Email:", tupla[chave][1])
    nome = input("Digite o seu nome: ")
    nivel = input("Digite o seu nivel: ")
    usuarios[tupla[chave][1]] = [nome, nivel]


for chave, dado in usuarios.items():
   
    print(f"Usuario......", {chave[0]})
    print(f"Email......", {chave[1]})
    print(f"Nome.....", {dado[0]})
    print(f"Nivel......", {dado[1]})

# ------[chave] -> Escolhe qual usuário da lista estamos acessando (o 1º, o 2º, etc.)

# ---------[1] -> Pega o e-mail que está guardado dentro da tupla do enumerate

# ---------[0] -> Pega a primeira informação da lista (o Nome)

# --------[1] -> Pega a segunda informação da lista (o Nível)