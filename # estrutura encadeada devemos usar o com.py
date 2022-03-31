# estrutura encadeada  devemos usar o comando "elif", que é uma abreviação de else
codigo_compra = 5444
if codigo_compra == 5222:
    print("compra a vista.")
elif codigo_compra == 5333:
    print("compra a prazo no boleto.")
elif codigo_compra ==5444:
    print("compra a prazo no cartao.")
else:
  print("código não cadastrado")
