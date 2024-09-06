from cidade import Cidade
import numpy as np

# def criando_cidades(n:int, cap:int) -> list:
#     cidades:list = []
#     for i in range(n):
#         valor = np.random.exponential(scale=10_000)
#         demanda_aleatoria:int = int(max(1_000, min(60_000, valor)))
#         coordenada_aleatoria:list = [random.randint(-100, 100), random.randint(-100, 100)]
#         tera_infra:bool = False
#         qtd_equi:int = 0
#         if demanda_aleatoria > 7_500: # A menor cidade no artigo possui 15 mil de população, então este número poderia ser até menor
#             tera_infra = True # Pensando em talvez colocar uma função que dependa da demanda, mas não seja assim tão preto no branco
#             qtd_equi = random.randint(0, int(demanda_aleatoria/cap) + 1) # O +1 é para possuir a chance de alguma cidade já possuir mais mamógrafos do que o necessário
#         nova_cidade:Cidade = Cidade(coordenada_aleatoria,demanda_aleatoria,tera_infra,qtd_equi,i,0.6)
#         cidades.append(nova_cidade)
#     return cidades

def criando_cidades() -> list:
    cidades = []
    #                        id  nome            coordenadas  dem  infra qtd_equip txMin micro
    cidades.append(Cidade(1, "Alta Floresta d'Oeste",  [-11.929187, -61.994242], 1887, True, 0, 0.6, 6)) 
    cidades.append(Cidade(2, "Alto Alegre dos Parecis", [-12.132608, -61.856679], 813, False, 0, 0.6, 6))
    cidades.append(Cidade(3, "Alto Paraíso", [-9.724708, -63.319058], 1224, True, 0, 0.6, 3))
    cidades.append(Cidade(4, "Alvorada d'Oeste", [-11.348088, -62.287770], 1345, False, 0, 0.6, 5))
    cidades.append(Cidade(5, "Ariquemes", [-9.906218, -63.033006], 6941, True, 0, 0.6, 3))
    cidades.append(Cidade(6, "Buritis", [-10.194703, -63.833030], 1823, True, 0, 0.6, 1))
    cidades.append(Cidade(7, "Cabixi", [-13.494663, -60.542529], 541, False, 0, 0.6, 8))
    cidades.append(Cidade(8, "Cacaulândia", [-10.341931, -62.900039], 425, False, 0, 0.6, 3))
    cidades.append(Cidade(9, "Cacoal",  [-11.434667, -61.456662], 6618, True, 0, 0.6, 6))
    cidades.append(Cidade(10, "Campo Novo de Rondônia", [-10.570198, -63.618943], 605, False, 0, 0.6, 1))
    cidades.append(Cidade(11, "Candeias do Jamari", [-8.795812, -63.700415], 1400, True, 0, 0.6, 1))
    cidades.append(Cidade(12, "Castanheiras", [-11.426685, -61.949017], 261, False, 0, 0.6, 6))
    cidades.append(Cidade(13, "Cerejeiras", [-13.189004, -60.820803], 1439, True, 0, 0.6, 8))
    cidades.append(Cidade(14, "Chupinguaia", [-12.555151, -60.902296], 546, False, 0, 0.6, 7))
    cidades.append(Cidade(15, "Colorado do Oeste", [-13.120983, -60.545008], 1577, True, 0, 0.6, 8))
    cidades.append(Cidade(16, "Corumbiara", [-12.998581, -60.946000], 657, False, 0, 0.6, 8))
    cidades.append(Cidade(17, "Costa Marques", [-12.435720, -64.229452], 750, False, 0, 0.6, 2))
    cidades.append(Cidade(18, "Cujubim", [-9.368920, -62.583042], 848, False, 0, 0.6, 1))
    cidades.append(Cidade(19, "Espigão d'Oeste", [-11.525725, -61.011626], 2210, True, 0, 0.6, 6))
    cidades.append(Cidade(20, "Governador Jorge Teixeira", [-10.612193, -62.733130], 787, False, 0, 0.6, 4))
    cidades.append(Cidade(21, "Guajará-Mirim",  [-10.789321, -65.330105], 2928, True, 0, 0.6, 2))
    # cidades.append(Cidade(22, "Itapuã do Oeste", [-9.188610, -63.185665], 545, False, 0, 0.6, 1))
    # cidades.append(Cidade(23, "Jaru", [-10.428357, -62.473662], 3983, True, 0, 0.6, 4))
    # cidades.append(Cidade(24, "Ji-Paraná", [-10.878141, -61.932673], 9730, True, 0, 0.6, 4))
    # cidades.append(Cidade(25, "Machadinho d'Oeste", [-9.425200, -62.002465], 2014, True, 0, 0.6, 3))
    # cidades.append(Cidade(26, "Ministro Andreazza", [-11.197720, -61.517137], 747, False, 0, 0.6, 6))
    # cidades.append(Cidade(27, "Mirante da Serra", [-11.030540, -62.672987], 727, False, 0, 0.6, 4))
    # cidades.append(Cidade(28, "Monte Negro", [-10.260447, -63.297931], 994, False, 0, 0.6, 3))
    # cidades.append(Cidade(29, "Nova Brasilândia d'Oeste", [-11.725939, -62.311619], 1176, True, 0, 0.6, 5))
    # cidades.append(Cidade(30, "Nova Mamoré", [-10.410668, -65.330562], 1502, True, 0, 0.6, 1))
    # cidades.append(Cidade(31, "Nova União", [-10.915446, -62.556989], 542, False, 0, 0.6, 4))
    # cidades.append(Cidade(32, "Novo Horizonte do Oeste", [-11.707210, -61.998303], 624, False, 0, 0.6, 6))
    # cidades.append(Cidade(33, "Ouro Preto do Oeste", [-10.720916, -62.255980], 3162, True, 0, 0.6, 4))
    # cidades.append(Cidade(34, "Parecis", [-12.181705, -61.604288], 281, False, 0, 0.6, 7))
    # cidades.append(Cidade(35, "Pimenta Bueno", [-11.677457, -61.178759], 2787, True, 0, 0.6, 7))
    # cidades.append(Cidade(36, "Pimenteiras do Oeste", [-13.481384, -61.046885], 169, False, 0, 0.6, 8))
    # cidades.append(Cidade(37, "Porto Velho", [-8.763547, -63.897172], 33075, True, 0, 0.6, 1))
    # cidades.append(Cidade(38, "Presidente Médici", [-11.169147, -61.901666], 1935, True, 0, 0.6, 4))
    # cidades.append(Cidade(39, "Primavera de Rondônia", [-11.830201, -61.319260], 288, False, 0, 0.6, 7))
    # cidades.append(Cidade(40, "Rio Crespo", [-9.705509, -62.899774], 241, False, 0, 0.6, 3))
    # cidades.append(Cidade(41, "Rolim de Moura", [-11.725698, -61.778141], 4117, True, 0, 0.6, 6))
    # cidades.append(Cidade(42, "Santa Luzia d'Oeste", [-11.906444, -61.779729], 763, False, 0, 0.6, 6))
    # cidades.append(Cidade(43, "São Felipe d'Oeste", [-11.906359, -61.513658], 493, False, 0, 0.6, 7))
    # cidades.append(Cidade(44, "São Francisco do Guaporé", [-12.060075, -63.569186], 1022, True, 0, 0.6, 2))
    # cidades.append(Cidade(45, "São Miguel do Guaporé", [-11.693908, -62.714513], 1451, 1, 0, 0.6, 5))
    # cidades.append(Cidade(46, "Seringueiras", [-11.765474, -63.031444], 777, False, 0, 0.6, 5))
    # cidades.append(Cidade(47, "Teixeirópolis", [-10.932702, -62.254667], 380, False, 0, 0.6, 4))
    # cidades.append(Cidade(48, "Theobroma", [-10.242790, -62.351833], 784, False, 0, 0.6, 4))
    # cidades.append(Cidade(49, "Urupá", [-11.124309, -62.363572], 1000, False, 0, 0.6, 4))
    # cidades.append(Cidade(50, "Vale do Anari", [-9.859641, -62.174804], 677, False, 0, 0.6, 3))
    # cidades.append(Cidade(51, "Vale do Paraíso", [-10.427401, -62.129765], 640, False, 0, 0.6, 4))
    # cidades.append(Cidade(52, "Vilhena", [-12.738459, -60.122151], 6187, True, 0, 0.6, 7))
    return cidades

def matriz_distancias(n:int, cidades:list) -> list:
    distancias = np.zeros((n, n))
    for i in range(len(cidades) - 1):
        for j in range(1,len(cidades)):
            distancia_aux = cidades[i].calc_dist(cidades[j].coordenadas)
            distancias[i][j] = distancia_aux
            distancias[j][i] = distancia_aux
    return distancias

# def criar_micro_regioes(cidades:list, matriz_distancias:list) -> None:
#     micro = {}
#     cidades_com_infra = [cidade for cidade in cidades if cidade.infra]
#     for cidade in cidades_com_infra:
#         cidade.micro = cidade.id
#         micro[cidade.id] = [cidade]

#     # Atribuir cada cidade sem infraestrutura ao grupo mais próximo
#     for i, cidade in enumerate(cidades):
#         if not cidade.infra:
#             distancias = [matriz_distancias[i][cidade.id] for cidade in cidades_com_infra]
#             cidade_mais_proxima_idx = np.argmin(distancias)
#             idx_cidade_com_infra = [j for j in range(len(cidades)) if cidades[j].infra][cidade_mais_proxima_idx]
#             cidade.micro = cidades[idx_cidade_com_infra].id
#             micro[cidades[idx_cidade_com_infra].id].append(cidade)
            
#     for cidade in cidades:
#         cidade.S = micro[cidade.micro]

def criando_vetores_microrregiao(cidades:list, matriz_distancias:list, R:float) -> None:
    for i, cidade in enumerate(cidades):
        for j, outra_cidade in enumerate(cidades):
            if cidade.micro == outra_cidade.micro and matriz_distancias[i][j] <= R and matriz_distancias[j][i] <= R:
                cidade.S.append(outra_cidade.id - 1)

def calculo_dem_reg(cidades:list, matriz_distancias:list, R:float) -> None:
    for i, cidade in enumerate(cidades):
        dem_reg_total = 0
        for j, outra_cidade in enumerate(cidades):
            if matriz_distancias[i][j] < R:
                dem_reg_total += outra_cidade.dem
        cidade.demReg = dem_reg_total

# def criar_dados(N:int, cap:int, R:float) -> dict:
#     cidades = criando_cidades(N, cap)
#     d_ij = matriz_distancias(N, cidades)
#     criar_micro_regioes(cidades,d_ij)
#     calculo_dem_reg(cidades,d_ij,R)

#     return {
#         "cidades": cidades,
#         "d_ij": d_ij
#     }

def coletar_dados(R:float) -> dict:
    cidades = criando_cidades()
    N = len(cidades)
    d_ij = matriz_distancias(N, cidades)
    criando_vetores_microrregiao(cidades, d_ij, R)
    calculo_dem_reg(cidades, d_ij, R)
    return {
        "cidades": cidades,
        "d_ij": d_ij
    }

def __main__():
    R = 60.0
    cidades = criando_cidades()
    N = len(cidades)
    dij = matriz_distancias(N, cidades)
    criando_vetores_microrregiao(cidades,dij,R)
    calculo_dem_reg(cidades,dij,R)

    print(cidades[4])
    print(cidades[2])
    print(dij[4][2])
    print('\n')
    print(cidades[4])
    print(cidades[7])
    print(dij[4][7])
    print('\n')
    print(cidades[4])
    print(cidades[27])
    print(dij[4][27])
    print('\n')
    print(cidades[4])
    print(cidades[39])
    print(dij[4][39])
    
if __name__ == "__main__":
    __main__()