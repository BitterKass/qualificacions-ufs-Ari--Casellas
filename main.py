# Definició de classes
from modul_profesional import ModulProfessional
from unitat_formativa import UnitatFormativa


def inicialitzar_modul_professional():
    global uf1, uf2, uf3, mp5
    uf1 = UnitatFormativa("UF1. Desenvolupament del programari", 20)
    uf2 = UnitatFormativa("UF2. Optimització del programari", 20)
    uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes", 26)
    uf1.qualificacio = 8
    uf2.qualificacio = 10
    uf3.qualificacio = 4
    mp5 = ModulProfessional("MP05. Entorns de desenvolupament")
    mp5.afegir_unitat_formativa(uf1)
    mp5.afegir_unitat_formativa(uf2)
    mp5.afegir_unitat_formativa(uf3)


def mostrar_dades_modul_professional():
    print(uf1.nom, ":", uf1.qualificacio)
    print(uf2.nom, ":", uf2.qualificacio)
    print(uf3.nom, ":", uf3.qualificacio)
    print(mp5.nom, ":", mp5.get_qualificacio())


# Inici del programa
inicialitzar_modul_professional()
mostrar_dades_modul_professional()