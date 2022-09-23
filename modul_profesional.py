class ModulProfessional:
    nom = None
    unitats_formatives = []

    def __init__(self, nom):
        self.nom = nom

    def afegir_unitat_formativa(self, unitat_formativa):
        self.unitats_formatives.append(unitat_formativa);

    def get_qualificacio(self):
        suma_hores = 0
        suma_qualificacio = 0

        for uf in self.unitats_formatives:
            suma_hores += uf.hores
            suma_qualificacio += (uf.qualificacio * uf.hores)

        return suma_qualificacio / suma_hores
