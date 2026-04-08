base_dados = []
with open("iris.data", "r") as arquivo: 
     for registro in arquivo.readlines():
        base_dados.append(registro.split(","))

print(base_dados)

print(float(base_dados[0] [0]) + float(base_dados [0] [1]))

# O .split() serve para quebrar as linhas/separar ---- Exemplo ("Eu amo python") -- Ele deixaria assim ---- ["Eu", "amo", "python"]


# esse codigo serve para abrir um, arquivo! Pode ser usado diversar letrinhas para abri-lós, como r, w, a, x. 
# O r serve para leitura, o w para escrita, o a para adicionar (Serve para leritura e escrita), e o x para exclusão(Só você manipula o arquivo, s´´o podem usar quando você fecha-lo).
# O rx ao inves de só escrever no arquivo, ele vai escrever e criar um novo arquivo.

#with open("Primeiro_Arquivo.txt", "r") as arquivo:
#    centeudo = arquivo.readline()
#    for linha in arquivo.readlines():
#        print(linha)


# usar o .read() para ler o conteúdo de um arquivo de texto. Assim, ele vai imprimir o que estiver dentro dele, e ele vai mostrar linha por linha.
# Esse codigo, trabalha linha a linha with open("Primeiro_Arquivo.txt", "r") as arquivo:
#centeudo = arquivo.readline()
#for linha in arquivo.readlines():
#print(linha)