

#nome = input("Digite um funcionário: ")
#
#empresa = input("Digite a instituição: ")
#
#qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
#
#mediaMensalidade = float(input("Digite a média da mensalidade: "))
#
#print(nome + " trabalha na empresa " + empresa)
#
#print("Possui: ", qtde_funcionarios, " funcionarios.")
#
#print("A média da mensalidade é de: " + str(mediaMensalidade))
#
#print("==============Verifique os tipos de dados abaixo:==============")
#
#print("O tipo de dado da variavel [nome] é: ", type(nome))
#
#print("O tipo de dado da variavel [empresa] é: ", type(empresa))
#
#print("O tipo de dado da variavel [qtde_funcionarios] é: ", type(qtde_funcionarios))
#
#print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))

# APRENDENDO (DECISÃO) IF, ELIF E ELSE ------------------------------------------------------------------------

#nome = input("Digite o seu nome: ")
#idade = int(input("Digite a sua idade: "))
#if idade >= 65:
#    print("Paciente", nome, "POSSUI atendimento prioritario.")
#else:
#    print("Paciente", nome, "NÃO possui atendimento prioritario.")

# APRENDENDO LAÇOS DE REPETIÇÃO (WHILE E FOR) ------------------------------------------------------------------------

#numero = int(input("Digite um numero: "))
#while numero < 100:
#    print(str(numero))
#    numero = numero + 1 
#print("Laço encerrado")

#tabuada = int(input("Digite um numero para ver sua tabuada: "))
#print("Tabuada do", tabuada)
#for valor in range(1,11,1):
#    print(str(tabuada) + "X" + str(valor) + "=" + str((tabuada*valor)) )

#O range(valor, limite, passo) gera uma sequência de números. Os parâmetros são:
#valor: o primeiro número da sequência (por padrão, 0).
#limite: o número que determina quando a iteração do loop deve parar. Os números gerados são menores que o limite.
#passo: a quantidade que o contador é incrementado (ou decrementado, se for negativo) a cada iteração do loop. Por padrão, é 1.
#Por exemplo, range(1, 11, 1) gera uma sequência de números de 1 a 10. range(5, 16, 2) gera uma sequência de números de 5 a 15 com um passo de 2.

# LISTAS E VARIAVEIS --------------------------------------------------------------------------------------------

#O append agrega o item que foi respondido no input no - invetario[] -

#inventario = []
#resposta = "S"
#while resposta  == "S":
#    inventario.append(input("Equipamento: "))
#    inventario.append(float(input("Valor: ")))
#    inventario.append(int(input("numero serial: ")))
#    inventario.append(input("Departamento: "))
#    resposta = input("Digite \"S\" para continuar: ").upper()
#for elemento in inventario:
#    print(elemento)

# MULTIPLAS LISTAS E INDICES --------------------------------------------------------------------

# Usar [] para quando for -- LISTA -- (Guardar nomes, arquivos, salario, etc ...)

#equipamentos = []
#
#valores = []
#
#seriais = []
#
#departamentos = []
#
#resposta = "S"
#
#while resposta == "S":
#  equipamentos.append(input("Equipamento: "))
#
#  valores.append(float(input("Valor: ")))
#
#  seriais.append(int(input("Número Serial: ")))
#
#  departamentos.append(input("Departamento: "))
#
#  resposta = input("Digite \"S\" para continuar ou ENTER para parar: ").upper()
#
#busca=input("Digite o nome do equipamento que deseja buscar: ")
#
#for indice in range(0,len(equipamentos)):
#                                                     #Este código percorre uma lista equipamentos e verifica se um valor busca é igual a um dos elementos na lista. Se a condição for verdadeira, o código dentro do bloco if será executado.
#                                                     #Em resumo, este código é usado para buscar um valor específico na lista equipamentos e executar uma ação se o valor for encontrado.
#                                                    #A função range(0, len(equipamentos)) gera uma sequência de números de 0 até len(equipamentos) - 1, que é o número total de elementos na lista equipamentos.
#                                                    #O loop for indice in range(0, len(equipamentos)): itera sobre essa sequência de números e atribui cada número a uma variável chamada indice.
#                                                    #Em cada iteração do loop, a variável indice recebe o valor do índice atual durante a iteração. Por exemplo, no primeiro itero, indice recebe 0, no segundo itero, indice recebe 1, e assim por diante.
#                                                    #Dentro do loop for, você pode usar a variável indice para acessar os elementos da lista equipamentos usando o índice atual. Por exemplo, equipamentos[indice] retorna o elemento da lista equipamentos correspondente ao índice atual.
#
#  if busca==equipamentos[indice]:
#    print("Valor..: ", valores[indice])
#    print("Serial.:", seriais[indice])



#inventario=[]
#resposta = "S"
#while resposta == "S":
#  equipamento=[input("Equipamento: "),
#            float(input("Valor: ")),
#            int(input("Número Serial: ")),
#            input("Departamento: ")]
#  inventario.append(equipamento)
#
#  resposta = input("Digite \"S\" para continuar: ").upper()
#
#for elemento in inventario:
#  print("Nome.........: ", elemento[0])
#  print("Valor........: ", elemento[1])
#  print("Serial.......: ", elemento[2])
#  print("Departamento.: ", elemento[3])
#
#busca=input("Digite o nome do equipamento que deseja buscar: ")
#for elemento in inventario:
#  if busca==elemento[0]:
#    print("Valor..: ", elemento[1])
#    print("Serial.:", elemento[2])
#
#depreciacao=input("Digite o nome do equipamento que será depreciado: ")
#for elemento in inventario:
#  if depreciacao==elemento[0]:
#    print("Valor antigo: ", elemento[1])
#    elemento[1] = elemento[1] * 0.9
#    print("Novo valor: ", elemento[1])
#
#serial=int(input("Digite o serial do equipamento que será excluído: "))
#for elemento in inventario:
#  if elemento[2]==serial:
#    inventario.remove(elemento)
#
#for elemento in inventario:
#  print("Nome.........: ", elemento[0])
#  print("Valor........: ", elemento[1])
#  print("Serial.......: ", elemento[2])
#  print("Departamento.: ", elemento[3]) 
#
#valores=[]
#for elemento in inventario:
#  valores.append(elemento[1])
#if len(valores)>0:
#  print("O equipamento mais caro custa: ", max(valores))
#  print("O equipamento mais barato custa: ", min(valores))
#  print("O total de equipamentos é de: ", sum(valores))

    