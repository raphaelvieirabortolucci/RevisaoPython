#objetivo: usar tudo ou quase tudo do basico 
listaHeroi = []
listaMonstro = []

while True:
    print("escolha uma das opcoes baixo")
    print('1-adicionar... ')
    print('2-remover... ')
    print('3-mostrar... ')
    print('4-sair')

    escolha = input("digite o numero da funcao desejada: ")

    if escolha == "1":
    
        while True:
            print("escolha qual dessa opcoes voce vai quer adicionar um ficha")
            print("1-ficha de heroi")
            print("2-ficha de monstro")
            print("3-sair")
            escolha2 = input("digite o quer criar: ") 
            
            if escolha2 == "1":
                nomeHeroi = input("digite o nome do heroi: ")
                generoHeroi = input("digite o genero do heroi: ")
                racaHeroi = input("digite a raca do heroi: ")
                forcaHeroi = int(input("digite a forca do heroi de 0 a 5: "))
                while True:

                    if 0 <= forcaHeroi <= 5:
                        break

                    else:
                        print('digite um numero de 0 a 5')
                        forcaHeroi = int(input("digite a forca do heroi de 0 a 5: "))

                inteligenciaHeroi = int(input("digite a inteligencia do heroi de 0 a 5: "))
                while True:
                            
                    if 0 <= inteligenciaHeroi <= 5:
                        break
                
                    else:
                        print('digite um numero de 0 a 5')
                        inteligenciaHeroi = int(input("digite a inteligencia do heroi de 0 a 5: "))
                destrezaHeroi = int(input("digite a destreza do heroi de 0 a 5: "))
                while True:
                            
                    if 0 <= destrezaHeroi <= 5:
                        break

                    else:
                        print('digite um numero de 0 a 5')
                        destrezaHeroi = int(input("digite a destreza do heroi de 0 a 5: "))

                carismaHeroi = int(input("digite a carisma do heroi de 0 a 5: "))
                while True:
                                        
                    if 0 <= carismaHeroi <= 5:
                        break
                
                    else:
                        print('digite um numero de 0 a 5')
                        carismaHeroi = int(input("digite a carisma do heroi de 0 a 5: "))

                magiaHeroi = int(input("digite a magia do heroi de 0 a 5: "))
                while True:
                                        
                    if 0 <= magiaHeroi <= 5:
                        break
                
                    else:
                        print('digite um numero de 0 a 5')
                        magiaHeroi = int(input("digite a magia do heroi de 0 a 5: "))

                fichaHeroi = {
                "nome": nomeHeroi,
                "raca": racaHeroi,
                "genero": generoHeroi,
                "forca": forcaHeroi,
                "inteligencia": inteligenciaHeroi,
                "destreza": destrezaHeroi,
                "carisma": carismaHeroi,
                "magia": magiaHeroi
                }

                listaHeroi.append(fichaHeroi)

            elif escolha2 == "2":
                nomeMonstro = input("digite o nome do Monstro: ")
                generoMonstro = input("digite o genero do Monstro: ")
                racaMonstro = input("digite a raca do Monstro: ")
                forcaMonstro = int(input("digite a forca do Monstro de 0 a 5: "))
                while True:
                                
                    if 0 <= forcaMonstro <= 5:
                        break
                
                    else:
                        print('digite um numero de 0 a 5')
                        forcaMonstro = int(input("digite a forca do Monstro de 0 a 5: "))

                inteligenciaMonstro = int(input("digite a inteligencia do Monstro de 0 a 5: "))
                while True:
                                        
                    if 0 <= inteligenciaMonstro <= 5:
                        break
                            
                    else:
                        print('digite um numero de 0 a 5')
                        inteligenciaMonstro = int(input("digite a inteligencia do Monstro de 0 a 5: "))

                destrezaMonstro = int(input("digite a destreza do Monstro de 0 a 5"))
                while True:
                                        
                    if 0 <= destrezaMonstro <= 5:
                        break
                
                    else:
                        print('digite um numero de 0 a 5')
                        destrezaMonstro = int(input("digite a destreza do Monstro de 0 a 5: "))
                
                carismaMonstro = int(input("digite a carisma do Monstro de 0 a 5: "))
                while True:
                                                    
                    if 0 <= carismaMonstro <= 5:
                        break
                            
                    else:
                        print('digite um numero de 0 a 5')
                        carismaMonstro = int(input("digite a carisma do Monstro de 0 a 5"))
                
                magiaMonstro = int(input("digite a magia do Monstro de 0 a 5"))
                while True:
                                                    
                    if 0 <= magiaMonstro <= 5:
                        break
                            
                    else:
                        print('digite um numero de 0 a 5')
                        magiaMonstro = int(input("digite a magia do Monstro de 0 a 5"))
                
                fichaMonstro = {
                "nome": nomeMonstro,
                "raca": racaMonstro,
                "genero": generoMonstro,
                "forca": forcaMonstro,
                "inteligencia": inteligenciaMonstro,
                "destreza": destrezaMonstro,
                "carisma": carismaMonstro,
                "magia": magiaMonstro
                }  

                listaMonstro.append(fichaMonstro)

            elif escolha2 == "3":
                print("cancelando")
                break

            else:
                print("Opcao invalidade")


    elif escolha == "2":
        escolha3 = input("escolha um deles pare remover: ")
        print("3-Heroi")
        print("2-Monstro")
        print("1-sair")

        if escolha3 == "1":
            for fichaHeroi in listaHeroi:
                print(fichaHeroi["nome"])
            remover = input("digite o que quer remover: ")
            listaHeroi.remove(remover)

        elif escolha3 == "2":
            print(listaMonstro)
            remover = input("digite o que quer remover: ")
            listaMonstro.remove(remover)

    elif escolha == "3":
        print("1-heroi")
        print("2-monstro")
        escolha4 = input("qual opcao: ")

        if escolha4 == "1":
            print(f"as fichas sao: {enumerate(listaHeroi)}")
            print(f"o numero de fichas sao: {len(listaHeroi)}")
            

        elif escolha4 == "2":
            print(f"as fichas sao: {listaMonstro}")
            print(f"o numero de fichas sao: {len(listaMonstro)}")
            

    elif escolha == "4":
        print("encerrando programa...")
        break

    else:
        print("opcao invalida")    