nome = input("Digite seu nome:") #modo 1 de imprimir
print (nome)
print ("Ola, %s, seja bem vindo ao tutorial" % (nome))
apelido = input("como voce deseja ser chamado?")
print (apelido)
print (" ola novamente %s, voce is o cara"% (apelido))


nome = input("Digite seu nome:") #modo 2 de imprimir
print("ola {}, bem vindo a disciplina de programacao. parabens pelo seu primeiro hello world".format(nome))

nome = input("write your name here, please:") # modo 3 de imprimir, porem reconhecida pelo pep f strings
print(f"hello my friend, {nome}, wellcome to school")