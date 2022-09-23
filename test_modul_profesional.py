from unittest import TestCase

from modul_profesional import ModulProfessional
from unitat_formativa import UnitatFormativa


class TestModulProfessional(TestCase):
    def test_get_qualificacio(self):
        mp = ModulProfessional("Prova de mòdul professional");
        uf1 = UnitatFormativa("UF1", 10);
        uf1.qualificacio = 0
        uf2 = UnitatFormativa("UF2", 40);
        uf2.qualificacio = 10
        mp.afegir_unitat_formativa(uf1)
        mp.afegir_unitat_formativa(uf2)
        self.assertEqual(mp.get_qualificacio(), 8)