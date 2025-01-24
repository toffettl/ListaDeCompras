listaCompras = []

while True:
    resp = input("[i]nserir [a]pagar [l]istar ")
    if resp == "i":
        inserir = input("Oq vc deseja inserir? ")
        listaCompras.append(inserir)
        print(listaCompras)
    elif resp == "a":
         apagar = input("Digite o indice que deseja apagar: ")
         apagar = int(apagar)
         del listaCompras[apagar]
         print(listaCompras)
    elif resp == "l":
        print(listaCompras)
    else:
        print("Resposta inválida!")

         
