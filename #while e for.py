#while e for são estruturas de repetições. em uma estrutura de repetição haverá uma estrutura de decisão, pois a repetição de um trecho de código sempre está associada a uma condição.
#ou seja a condição imposta pelo dev será responsavel pela repetição ou não do bloco de comandos
numero = 1
while numero !=0:
  numero = int(input("Digite um Numero:"))
  if numero % 2 == 0:
    print("Numero par!")
  else:
    print("Numero ímpar!")