#Separar os textos
texto = "Gui e Juh"
        #0123456789
print(texto[0:4:2])
# Oque significa o [0:4]? Mostra que o print vai pegar os caracteres 0 á 4 da minha variavel ' texto'; após isso tem os ':' que significa que vai de x até = : y 
print(texto[5:])

print(texto[::-1])
# Se eu coloco dentro do [:: -1] ele vai mostrar o texto ao contrario

# vamos entende [0:4:2] -- Funciona como? O [Primeiro é a posição iicial: Quantidade de informação á percorrer: Pulando de quantos em quantos (Estava pulando de 2 em 2 casas")]

# Usar .find() para encontrar um texto/algo dentro de um texto(Variavel('Pode ser tudo')) --- O .find divido no momento em que vc pediu, então após isso, iniciasse a contagem novamente -- Ex: "Eu amo python" -- Como pedimos a letra "O", após achar em ele começa a contar de novo!!
# Se usa apenas Ex: texto = "Eu amo python"                                                                                                                                                      0123450123450
#                   print(texto.find("o")) -- Ele vai encontrar o primeiro 'o' que está em "Eu am'O' python"
#---------------------------------------------------------------------------------------------------------------
# Agora para encontrar o ultimo 'O':
#                  texto = "Eu amo python"
#                  print(texto[texto.find("o") + 1:] .find("o"))
#      Ele vai encontrar o 2° 'O', que está em "Eu amo pyth'O'n" ---- Para "Cortar e ele encontrar o proximo 'O' usamos um outro texto fora dos (), após, [], acabando de encontrar o primeiro "O". Você adiciona +1 e utiliza outro .find("o"). Logo, fica assim ---- (texto[texto.find("o") + 1:] .find("o"))

# O .split() serve para quebrar as linhas/separar ---- Exemplo ("Eu amo python") -- Ele deixaria assim ---- ["Eu", "amo", "python"]