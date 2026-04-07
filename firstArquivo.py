# esse codigo serve para abrir um, arquivo! Pode ser usado diversar letrinhas para abri-lós, como r, w, a, x. 
# O r serve para leitura, o w para escrita, o a para adicionar (Serve para leritura e escrita), e o x para exclusão(Só você manipula o arquivo, s´´o podem usar quando você fecha-lo).
# O rx ao inves de só escrever no arquivo, ele vai escrever e criar um novo arquivo.

with open("Primeiro_Arquivo.txt", "r") as arquivo:
    centeudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)


# usar o .read() para ler o conteúdo de um arquivo de texto. Assim, ele vai imprimir o que estiver dentro dele, e ele vai mostrar linha por linha.
# Esse codigo, trabalha linha a linha with open("Primeiro_Arquivo.txt", "r") as arquivo:
#centeudo = arquivo.readline()
#for linha in arquivo.readlines():
#print(linha)



