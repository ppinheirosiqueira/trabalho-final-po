import gurobipy as gp
from gurobipy import GRB
from dados import coletar_dados

## Deixando os dados livres já que são globais e imutáveis
## Dados
N = -1             # Conjunto de localidades
d_ij = []          # Distância entre as localidades i e j, em km
dem_i = []         # Demanda anual por exames de mamografia da localidade i ∈ N
cap = 6_758        # Capacidade anual de realização de exames de um mamografo
pMax = 30          # Numero maximo de mamógrafos disponíveis para alocação
R = 60.0           # Distância m ́axima para atendimento, em km
infra_i = []       # Parâmetro que assume o valor 1 se a localidade i ∈ N possui infraestrutura para sediar mamógrafos, e 0 caso contrário
micro_i = []       # Microrregião de saúde à qual pertence a localidade i ∈ N
S_i = []           # Conjunto das localidades que estao na mesma microrregião de saúde da localidade i ∈ N e que distam Rkm dela, isto ́e: Si= {j ∈ N | dij ≤ R, dji ≤ R e micro j = micro i}
demReg_i = []      # Demanda anual por exames de mamografia das localidades que distam Rkm da localidade i ∈ N
txMin_i = []       # Taxa de utilização mínima requerida para instalação de um mamógrafo na localidade i ∈ N para atender as localidades que distam Rkm dela, em %
txViab = 0.6       # Taxa de viabilidade que justifica a aquisição de um novo equipamento, em %
nEquipExist_i = [] # Número de equipamentos existentes na localidade i ∈ N
#bigM = 10000       # Número inteiro positivo que assume no máximo o valor R, em km - NÃO PRECISA DE ACORDO COM O ANDRÉ, POSSO COLOCAR R NO LUGAR

dem_total = 0
auxDados = {}

def aux_main(tipo_binario: bool, R_aux:float = 60.0):
    global N, d_ij, dem_i, R, infra_i, micro_i, S_i, demReg_i, txMin_i, nEquipExist_i, auxDados, dem_total
    R = R_aux
    auxDados = coletar_dados(R)

    N = len(auxDados["cidades"])
    d_ij = auxDados["d_ij"]
    
    dem_i = []
    infra_i = [] 
    micro_i = [] 
    S_i = [] 
    demReg_i = [] 
    txMin_i = [] 
    nEquipExist_i = []
    
    for cidade in auxDados["cidades"]:
        dem_i.append(cidade.dem)
        infra_i.append(cidade.infra)
        micro_i.append(cidade.micro)       
        S_i.append(cidade.S)           
        demReg_i.append(cidade.demReg)      
        txMin_i.append(cidade.txMin)  
        nEquipExist_i.append(cidade.nEquipExist)
    
    dem_total = 0
    
    for i in range(N):
        dem_total += dem_i[i]
    
    if tipo_binario:
        PLM_binario()
    else:
        PLM_continuo()

def PLM_binario():
    # Inicializando o modelo
    model = gp.Model("Minimizar compra de Mamógrafos")

    y = model.addVars(N, lb=0, vtype=GRB.INTEGER, name="y")    # Variável inteira que representa o número de equipamentos instalados no local i
    p = model.addVar(lb=0, vtype=GRB.INTEGER, name="p")        # Variável inteira que indica a quantidade total de mamógrafos a serem instalados
    z = model.addVars(N, vtype=GRB.BINARY, name="z")     # Variável binária que assume o valor 1 se a localidade i sedia algum equipamento de mamografia, e valor 0, caso contrário

    ## Para o PLM Binário:
    x = model.addVars(N, N, vtype=GRB.BINARY, name="x")  # Variável binária que assume o valor 1 se as mulheres do local j são atendidas por algum mamógrafo instalado no local i, e valor 0, caso contrário

    # Objetivo PLM Binário
    model.setObjective(
        gp.quicksum(
            dem_i[j] * x[i, j] for i in range(N) for j in S_i[i] # maximização da cobertura de exames
        ) - (p * cap * txViab) - ( # minimizar  o número de equipamentos a serem adquiridos, penalizando a aquisição de equipamentos que não atendam a uma taxa mínima de utilização que justifique economicamente, ou mesmo socialmente, a sua instalação
            gp.quicksum(d_ij[i][j] * x[i, j] for i in range(N) for j in S_i[i]) / (N * R) #  minimizar a distância total entre os locais indicados a sediar mamógrafos e os que são atendidos por esses equipamentos
        ), GRB.MAXIMIZE
    )
    
    add_restricoes(model, x, y, z, p)

    # Rodar em si o Gurobi
    # model.write("modelo.lp")

    model.optimize()
    
    dem_com_taxa_min = 0
    numero_maquinas = 0
    dem_calc = 0
    
    if model.status == GRB.OPTIMAL:
        for i in range(N):
            if z[i].X:
                print(f"{auxDados['cidades'][i]}:")
                print(f"Número de Mamógrafos: {y[i].X}")
                print("Mulheres atendidas por esses mamógrafos:")
                aux = 0
                for j in range(N):
                    if x[i, j].X:
                        aux += dem_i[j]
                        print(f"{auxDados['cidades'][j]}")
                print(f"% de utilização dos Mamógrafos: {100*aux/(cap*y[i].X)}")
                dem_calc += aux
                if aux/(cap*y[i].X) > txMin_i[i]:
                    dem_com_taxa_min += aux
                    numero_maquinas += y[i].X
                print("\n")
        print(f"Demanda atendendo a taxa de 60%: {dem_com_taxa_min}, cobertura: {100*dem_com_taxa_min/dem_total}")
        print(f"Demanda não atendendo a taxa de 60%: {dem_calc}, cobertura: {100*dem_calc/dem_total}")
        print(f"Quantidade de Máquinas Alocadas: p = {p.X}")
        print(f"Quantidade de Máquinas realmente Alocadas: p = {numero_maquinas}")
    
def PLM_continuo():
    # Inicializando o modelo
    model = gp.Model("Minimizar compra de Mamógrafos")

    y = model.addVars(N, lb=0, vtype=GRB.INTEGER, name="y")    # Variável inteira que representa o número de equipamentos instalados no local i
    p = model.addVar(lb=0, vtype=GRB.INTEGER, name="p")        # Variável inteira que indica a quantidade total de mamógrafos a serem instalados
    z = model.addVars(N, vtype=GRB.BINARY, name="z")     # Variável binária que assume o valor 1 se a localidade i sedia algum equipamento de mamografia, e valor 0, caso contrário

    ## Para o PLM contínuo:
    x = model.addVars(N, N, lb=0, ub=1, vtype=GRB.CONTINUOUS, name="x")  # Variável contínua  que assume um valor no intervalo [0, 1], que indica opercentual de atendimento ao local j por algum mamógrafo instalado no local
    t = model.addVars(N, N, vtype=GRB.BINARY, name="t")  # Variável binária que assume o valor 1 se as mulheres do local j são atendidas por algum aparelho instalado no local i, e valor 0, caso contrário

    # Objetivo PLM contínuo
    model.setObjective(
        gp.quicksum(
            dem_i[j] * x[i, j] for i in range(N) for j in S_i[i] 
            ) - (p * cap * txViab) - ( 
            gp.quicksum(d_ij[i][j] * t[i, j] for i in range(N) for j in S_i[i]) / (N * R)
        ), GRB.MAXIMIZE
    )

    add_restricoes(model, x, y, z, p)
    
    for i in range(N):
        for j in range(N):
            model.addConstr(t[i, j] >= x[i, j], f"R10_{i}_{j}") # Até eu por isso aqui nada atualizava o t, não fazia sentido ele existir como estava
            
    # Modificando para o valor que eles citam no artigo 10^-6
    model.setParam('MIPGap', 0.000001)

    model.write("modelo.lp")

    # Rodar em si o Gurobi
    model.optimize()

    dem_com_taxa_min = 0
    numero_maquinas = 0
    dem_calc = 0
    
    if model.status == GRB.OPTIMAL:
        for i in range(N):
            if z[i].X:
                print(f"{auxDados['cidades'][i]}:")
                print(f"Número de Mamógrafos: {y[i].X}")
                print("Porcentagem de mulheres atendidas por esses mamógrafos:")
                aux = 0
                for j in range(N):
                    if x[i, j].X > 0:
                        aux += dem_i[j] * x[i, j].X
                        print(f"{auxDados['cidades'][j]}: {x[i, j].X}")
                print(f"% de utilização dos Mamógrafos: {100*aux/(cap*y[i].X)}")
                dem_calc += aux
                if aux/(cap*y[i].X) > txMin_i[i]:
                    dem_com_taxa_min += aux
                    numero_maquinas += y[i].X
                print("\n")
        print(f"Demanda atendendo a taxa de 60%: {dem_com_taxa_min}, cobertura: {100*dem_com_taxa_min/dem_total}")
        print(f"Demanda não atendendo a taxa de 60%: {dem_calc}, cobertura: {100*dem_calc/dem_total}")
        print(f"Quantidade de Máquinas Alocadas: p = {p.X}")
        print(f"Quantidade de Máquinas realmente Alocadas: p = {numero_maquinas}")

def add_restricoes(modelo, x, y, z, p):
    # Restrições, pegar o número da equação no artigo e subtrair 1
    
    # OK - TESTADA INDIVIDUALMENTE
    # Restrição 1: Somatório de x_ij <= 1 para todo j em N
    for j in range(N):
        modelo.addConstr(gp.quicksum(x[i, j] for i in S_i[j]) <= 1, f"R1_{j}")

    # OK - TESTADA INDIVIDUALMENTE
    # Restrição 2: Somatório de y_i = p
    modelo.addConstr(gp.quicksum(y[i] for i in range(N)) == p, "R2")

    # OK - TESTADA INDIVIDUALMENTE
    # # Restrição 3: Demanda * x_ij <= Capacidade * y_i
    for i in range(N):
        modelo.addConstr(gp.quicksum(dem_i[j] * x[i, j] for j in S_i[i]) <= cap * y[i], f"R3_{i}")

    # OK - TESTADA INDIVIDUALMENTE
    # # Restrição 4: y_i >= nEquipExist_i (existência de equipamentos)
    for i in range(N):
        modelo.addConstr(y[i] >= nEquipExist_i[i], f"R4_{i}")

    # OK - TESTADA INDIVIDUALMENTE
    # # Restrição 5: y_i >= 1 se infra = 1 e demReg_i >= txMin_i * cap
    ## Essa restrição sem ter as infras corretas e as distâncias corretas quebra muito o sistema, diversas cidades começam a ter mamógrafos com % de utilização bem abaixo do desejado
    for i in range(N):
        if infra_i[i] and demReg_i[i] >= txMin_i[i] * cap:
            modelo.addConstr(y[i] >= 1, f"R5_{i}")

    # OK - TESTADA INDIVIDUALMENTE
    # # Restrição 6: y_i == 0 se infra = 0
    for i in range(N):
        if not infra_i[i]:
            modelo.addConstr(y[i] == 0, f"R6_{i}")

    # OK - TESTADA INDIVIDUALMENTE 
    # # Restrição 7: z_i >= y_i / pMax
    for i in range(N):
        modelo.addConstr(z[i] >= y[i] / pMax, f"R7_{i}")

    # OK - TESTADA INDIVIDUALMENTE
    # # Restrição 8: x_ii = z_i para todas as i
    for i in range(N):
        modelo.addConstr(x[i, i] == z[i], f"R8_{i}_{i}")

    # OK - TESTADA INDIVIDUALMENTE
    # # Restrição 9: z_i >= x_ij para todas as i e j
    for i in range(N):
        for j in range(N):
            modelo.addConstr(z[i] >= x[i, j], f"R9_{i}_{j}")
            
    # Restrições 10, 11, 12 e 13 já são marcadas quando crio as variáveis aqui no gurobi
    
def __main__():
    aux_main(False, 60.0)
    
if __name__ == "__main__":
    __main__()