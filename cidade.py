import math

class Cidade():
    nome:str
    coordenadas:list
    dem:int
    infra:bool
    micro:int
    S:list
    demReg:int
    nEquipExist:int
    txMin:float
    
    def __init__(self, id:int, nome:str, novas_coordenas:list, nova_demanda:int, tem_infra:bool, qtd_equip:int, txMin:float, microrregiao:int) -> None:
        self.id = id
        self.nome = nome
        self.coordenadas = novas_coordenas.copy()
        self.dem = nova_demanda
        self.infra = tem_infra
        self.nEquipExist = qtd_equip
        self.txMin = txMin
        self.micro = microrregiao
        self.S = []
        
    def calc_dist(self, coordenadas_outra_cidade:list) -> float:
        # Converter coordenadas de graus para radianos
        lat1, lon1, lat2, lon2 = map(math.radians, [self.coordenadas[0], self.coordenadas[1], coordenadas_outra_cidade[0], coordenadas_outra_cidade[1]])
        
        # Fórmula de Haversine
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        # Raio da Terra em quilômetros (pode ser 6371 ou 6378.1, dependendo da precisão desejada)
        r = 6378.1
        distancia = r * c
        
        # d = 2*r*math.asin((math.sin((lat2 - lat1)/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1)/2)**2)**(1/2))
        
        return distancia

    def print_micro(self) -> None:
        for cidade in self.S:
            print(cidade)

    def __str__(self) -> str:
        return f"{self.id}.{self.nome}"
    