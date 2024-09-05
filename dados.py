import random
from cidade import Cidade
import numpy as np


def criando_cidades(n:int, cap:int) -> list:
    cidades:list = []
    for i in range(n):
        valor = np.random.exponential(scale=10_000)
        demanda_aleatoria:int = int(max(1_000, min(60_000, valor)))
        coordenada_aleatoria:list = [random.randint(-100, 100), random.randint(-100, 100)]
        tera_infra:bool = False
        qtd_equi:int = 0
        if demanda_aleatoria > 7_500: # A menor cidade no artigo possui 15 mil de população, então este número poderia ser até menor
            tera_infra = True # Pensando em talvez colocar uma função que dependa da demanda, mas não seja assim tão preto no branco
            qtd_equi = random.randint(0, int(demanda_aleatoria/cap) + 1) # O +1 é para possuir a chance de alguma cidade já possuir mais mamógrafos do que o necessário
        nova_cidade:Cidade = Cidade(coordenada_aleatoria,demanda_aleatoria,tera_infra,qtd_equi,i,0.6)
        cidades.append(nova_cidade)
    return cidades

def matriz_distancias(n:int, cidades:list) -> list:
    distancias = np.zeros((n, n))
    for i in range(len(cidades) - 1):
        for j in range(1,len(cidades)):
            distancia_aux = cidades[i].calc_dist(cidades[j].coordenadas)
            distancias[i][j] = distancia_aux
            distancias[j][i] = distancia_aux
    return distancias

def criar_micro_regioes(cidades:list, matriz_distancias:list) -> None:
    micro = {}
    cidades_com_infra = [cidade for cidade in cidades if cidade.infra]
    for cidade in cidades_com_infra:
        cidade.micro = cidade.id
        micro[cidade.id] = [cidade]

    # Atribuir cada cidade sem infraestrutura ao grupo mais próximo
    for i, cidade in enumerate(cidades):
        if not cidade.infra:
            distancias = [matriz_distancias[i][cidade.id] for cidade in cidades_com_infra]
            cidade_mais_proxima_idx = np.argmin(distancias)
            idx_cidade_com_infra = [j for j in range(len(cidades)) if cidades[j].infra][cidade_mais_proxima_idx]
            cidade.micro = cidades[idx_cidade_com_infra].id
            micro[cidades[idx_cidade_com_infra].id].append(cidade)
            
    for cidade in cidades:
        cidade.S = micro[cidade.micro]

def calculo_dem_reg(cidades:list, matriz_distancias:list, distancia_maxima:float) -> None:
    for i, cidade in enumerate(cidades):
        dem_reg_total = 0
        for j, outra_cidade in enumerate(cidades):
            if matriz_distancias[i][j] < distancia_maxima:
                dem_reg_total += outra_cidade.dem
        cidade.dem_reg = dem_reg_total

def criar_dados(N:int, cap:int, R:float) -> dict:
    cidades = criando_cidades(N, cap)
    d_ij = matriz_distancias(N, cidades)
    criar_micro_regioes(cidades,d_ij)
    calculo_dem_reg(cidades,d_ij,R)

    return {
        "cidades": cidades,
        "d_ij": d_ij
    }

def __main__():
    N = 5
    cap = 6_758
    R = 60.0
    pMax = 30 # Arbitrário
    cidades = criando_cidades(N, cap)
    dij = matriz_distancias(N, cidades)
    criar_micro_regioes(cidades,dij)
    calculo_dem_reg(cidades,dij,R)
    for cidade in cidades:
        print(cidade)
        print(cidade.dem_reg)
        print(cidade.txMin)
        
if __name__ == "__main__":
    __main__()