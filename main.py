# Definició de classes
class UnitatFormativa:
    nom = None
    qualificacio = None
    hores = None

    def __init__(self, nom, hores):
        self.nom = nom
        self.hores = hores


class ModulProfessiona:
    nom = None
    unitats_formatives = []

    def __init__(self, nom):
        self.nom = nom

    def afegirUnitatFormativa(self, unitat_formativa):
        self.unitats_formatives.append(unitat_formativa);

    def getQualificacio(self):
        suma_hores = 0
        suma_qualificacio = 0

        for uf in self.unitats_formatives:
            suma_hores += uf.hores
            suma_qualificacio += (uf.qualificacio * uf.hores)

        return suma_qualificacio / suma_hores


# Inici del programa
uf1 = UnitatFormativa("UF1. Desenvolupament del programari", 20)
uf2 = UnitatFormativa("UF2. Optimització del programari", 20)
uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes", 26)

uf1.qualificacio = 8
uf2.qualificacio = 10
uf3.qualificacio = 4

mp5 = ModulProfessiona("MP05. Entorns de desenvolupament")

mp5.afegirUnitatFormativa(uf1)
mp5.afegirUnitatFormativa(uf2)
mp5.afegirUnitatFormativa(uf3)

print(uf1.nom, ":", uf1.qualificacio)
print(uf2.nom, ":", uf2.qualificacio)
print(uf3.nom, ":", uf3.qualificacio)
print(mp5.nom, ":", mp5.getQualificacio())


Anunci: .gitignore
Joan Rodriguez Bellido
Data de creació: 18:0418:04
.gitignore

.gitignore o cómo evitar que ciertos ficheros se añadan a tu repositorio Git
https://j2logo.com/gitignore-para-que-sirve/#


Anunci: Mètodes
Joan Rodriguez Bellido
Data de creació: 16 de set.16 de set.
Mètodes

poo_esquema.jpg (850×534)
https://programandoamimanera.com/wp-content/uploads/2019/11/poo_esquema.jpg


Anunci: # Definició de classes class…
Joan Rodriguez Bellido
Data de creació: 16 de set.16 de set.
# Definició de classes
class UnitatFormativa:
    nom = None
    nota = None

    def __init__(self, nom):
        self.nom = nom


# Inici del programa
uf1 = UnitatFormativa("UF1. Desenvolupament del programari")
uf2 = UnitatFormativa("UF2. Optimització del programari")
uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes")

uf1.nota = 8
uf2.nota = 10
uf3.nota = 4

print(uf1.nom, ":", uf1.nota)
print(uf2.nom, ":", uf1.nota)
print(uf3.nom, ":", uf1.nota)