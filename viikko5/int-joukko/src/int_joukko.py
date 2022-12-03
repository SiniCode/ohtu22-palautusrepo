class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if self.argumentit_kelpaavat(kapasiteetti, kasvatuskoko):
            self.kapasiteetti = kapasiteetti
            self.kasvatuskoko = kasvatuskoko
            self.taulukko = [0] * self.kapasiteetti
            self.alkioiden_lkm = 0
        else:
            raise Exception("Kapasiteetin ja kasvatuskoon tulee olla epänegatiivisia kokonaislukuja.")

    def argumentit_kelpaavat(self, kapasiteetti, kasvatuskoko):
        try:
            int(kapasiteetti)
            int(kasvatuskoko)
        except ValueError:
            return False
        
        return kapasiteetti >= 0 and kasvatuskoko >= 0

    def kuuluu(self, n):
        return n in self.taulukko

    def taulukko_on_taysi(self):
        return self.alkioiden_lkm == len(self.taulukko)

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.taulukko_on_taysi():
            self.taulukko = self.taulukko + [0] * self.kasvatuskoko

        self.taulukko[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        return True

    def poista(self, n):
        if self.kuuluu(n):
            self.taulukko.remove(n)
            self.taulukko = self.taulukko + [0]
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def listaa_luvut(self):
        int_list = self.taulukko[:self.alkioiden_lkm]
        return int_list

    @staticmethod
    def valmistele_joukot(int_joukko1, int_joukko2):
        tulosjoukko = IntJoukko()
        luvut1 = int_joukko1.listaa_luvut()
        luvut2 = int_joukko2.listaa_luvut()

        return tulosjoukko, luvut1, luvut2

    @staticmethod
    def yhdiste(int_joukko1, int_joukko2):
        yhdiste, luvut1, luvut2 = IntJoukko.valmistele_joukot(int_joukko1, int_joukko2)

        for luku in luvut1 + luvut2:
            yhdiste.lisaa(luku)

        return yhdiste

    @staticmethod
    def leikkaus(int_joukko1, int_joukko2):
        leikkaus, luvut1, luvut2 = IntJoukko.valmistele_joukot(int_joukko1, int_joukko2)

        for luku in luvut1:
            if luku in luvut2:
                leikkaus.lisaa(luku)

        return leikkaus

    @staticmethod
    def erotus(int_joukko1, int_joukko2):
        erotus, luvut1, luvut2 = IntJoukko.valmistele_joukot(int_joukko1, int_joukko2)

        for luku in luvut1:
            erotus.lisaa(luku)

        for luku in luvut2:
            erotus.poista(luku)

        return erotus

    def __str__(self):
        luvut = self.listaa_luvut()
        tuloste = str(luvut).replace("[", "{").replace("]", "}")
        return tuloste
