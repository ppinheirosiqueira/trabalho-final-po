from gurobi import aux_main

def __main__():
    while True:
        print("Opções: ")
        print("1 - PLM Binário")
        print("2 - PLM Contínuo")
        print("0 - Sair")
        escolha = input("Digite qual opção deseja executar: ")
        if escolha == "1":
            print("Opções: ")
            print("1 - R = 30.0")
            print("2 - R = 40.0")
            print("3 - R = 50.0")
            print("4 - R = 60.0")
            print("5 - R = 90.0")
            print("6 - R = 120.0")
            escolha_r = input("Digite qual opção deseja executar: ")
            if escolha_r == "1":
                aux_main(True,30.0)
            elif escolha_r == "2":
                aux_main(True,40.0)
            elif escolha_r == "3":
                aux_main(True,50.0)
            elif escolha_r == "4":
                aux_main(True,60.0)
            elif escolha_r == "5":
                aux_main(True,90.0)
            elif escolha_r == "6":
                aux_main(True,120.0)
            else:
                print("Por favor, digite um valor válido\n\n")
        elif escolha == "2":
            print("Opções: ")
            print("1 - R = 30.0")
            print("2 - R = 40.0")
            print("3 - R = 50.0")
            print("4 - R = 60.0")
            print("5 - R = 90.0")
            print("6 - R = 120.0")
            escolha_r = input("Digite qual opção deseja executar: ")
            if escolha_r == "1":
                aux_main(False,30.0)
            elif escolha_r == "2":
                aux_main(False,40.0)
            elif escolha_r == "3":
                aux_main(False,50.0)
            elif escolha_r == "4":
                aux_main(False,60.0)
            elif escolha_r == "5":
                aux_main(False,90.0)
            elif escolha_r == "6":
                aux_main(False,120.0)
            else:
                print("Por favor, digite um valor válido\n\n")
        elif escolha == "0":
            break
        else:
            print("Por favor, digite um valor válido\n\n")

    
if __name__ == "__main__":
    __main__()