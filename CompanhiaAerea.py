# CompanhiaAerea - Voos
class Voo:
    def __init__(self, num, orig, dest):
        self.__numero = num  # esse atributo é privado
        self.origem = orig
        self.destino = dest

    def get_origem(self):
        return self.origem

    def get_destino(self):
        return self.destino

    def get_numero(self):
        return self.__numero


class CompanhiaAerea:
    def __init__(self, cnpj, nome, qtde, *voos):
        self.__CNPJ = cnpj
        self.nome = nome
        self.numero_aeronaves = qtde
        self.listaVoos = []
        for e in voos:
            self.listaVoos.append(e)

    def get_nome(self):
        return self.nome

    def get_listaVoos(self):
        return self.listaVoos

    def add_voos(self, *novoVoo):
        for x in novoVoo:
            self.listaVoos.append(x)


# ========== Criação dos Objetos

v1 = Voo(1111, 'Curitiba', 'Ribeirão Preto')
v2 = Voo(2222, 'Campinas', 'Petrópolis')
v3 = Voo(3333, 'Curitiba', 'Fortaleza')
v4 = Voo(4444, 'Salvador', 'Mariana')

c1 = CompanhiaAerea('11.111.111\1111-11', 'Air Lines All', 120, v1, v2)
c2 = CompanhiaAerea('22.222.222\2222-22', 'Bon Jour', 20, v3, v4)

# listar os vôos cadastrados até o momento - por Companhia Aérea

lista = [c1, c2]

for c in lista:
    for e in c.listaVoos:
        print(c.nome, ' é responsável pelo vôo ', e.get_numero())

v5 = Voo(55555, 'Florianópolis', 'Curitiba')
v6 = Voo(6666, 'Curitiba', 'Porto Alegre')

c1.add_voos(v5, v6)

for c in lista:
    for e in c.listaVoos:
        print(c.nome, ' é responsável pelo vôo ', e.get_numero())






