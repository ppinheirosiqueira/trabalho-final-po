class Cidade():
    coordenadas:list
    dem:int
    infra:bool
    micro:int
    S:list
    demReg:int
    nEquipExist:int
    txMin:float
    
    def __init__(self, novas_coordenas:list, nova_demanda:int, tem_infra:bool, qtd_equip:int, id:int, txMin:float) -> None:
        self.coordenadas = novas_coordenas.copy()
        self.dem = nova_demanda
        self.infra = tem_infra
        self.nEquipExist = qtd_equip
        self.micro = -1
        self.id = id
        self.txMin = txMin
        
    def calc_dist(self, coordenadas_outra_cidade:list) -> float:
        return  ((coordenadas_outra_cidade[0] - self.coordenadas[0])**2 + (coordenadas_outra_cidade[1] - self.coordenadas[1])**2)**(1/2)

    def print_micro(self) -> None:
        for cidade in self.S:
            print(cidade)

    def __str__(self) -> str:
        infra_status = "sim" if self.infra else "não"
        return f"Cidade {self.id}: Coordenadas: {self.coordenadas}, Demanda: {self.dem}, Infraestrutura: {infra_status}, Microrregião: {self.micro}"
    