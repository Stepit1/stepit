class InterfataUtilizator:
    def __init__(self, aeroport):
        self.aeroport = aeroport

    def adauga_zbor(self, destinatie, ora_plecare, ora_sosire):
        zbor = Zbor(destinatie, ora_plecare, ora_sosire)
        self.aeroport.adauga_zbor(zbor)

    def verifica_status_zbor(self, destinatie):
        for zbor in self.aeroport.zboruri:
            if zbor.destinatie == destinatie:
                return zbor.verifica_status()
        return "Zborul nu a fost găsit."

    def afiseaza_informatii_terminal(self):
        return [terminal.afiseaza_detalii_terminal() for terminal in self.aeroport.terminale]

    def afiseaza_zboruri_disponibile(self):
        return self.aeroport.afiseaza_zboruri()

