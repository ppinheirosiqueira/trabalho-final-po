from gurobi import PLM_binario, PLM_continuo

def __main__():
    while True:
        print("Opções: ")
        print("1 - PLM Binário")
        print("2 - PLM Contínuo")
        escolha = input("Digite qual opção deseja executar: ")
        if escolha == "1":
            print("Opções: ")
            print("1 - R = 60.0")
            print("2 - R = 90.0")
            print("3 - R = 120.0")
            escolha_r = input("Digite qual opção deseja executar: ")
            if escolha_r == "1":
                PLM_binario()
            elif escolha_r == "2":
                PLM_binario(90.0)
            elif escolha_r == "3":
                PLM_binario(120.0)
            else:
                print("Por favor, digite um valor válido\n\n")
        elif escolha == "2":
            print("Opções: ")
            print("1 - R = 60.0")
            print("2 - R = 90.0")
            print("3 - R = 120.0")
            escolha_r = input("Digite qual opção deseja executar: ")
            if escolha_r == "1":
                PLM_continuo()
            elif escolha_r == "2":
                PLM_continuo(90.0)
            elif escolha_r == "3":
                PLM_continuo(120.0)
            else:
                print("Por favor, digite um valor válido\n\n")
        else:
            print("Por favor, digite um valor válido\n\n")

    
if __name__ == "__main__":
    __main__()