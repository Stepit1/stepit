class Terminal(Aeroport):
    def __init__(self, nume_aeroport, cod_IATA, locatie, numar_terminal, numar_porti_imbarcare):
        super().__init__(nume_aeroport, cod_IATA, locatie)
        self.numar_terminal = numar_terminal
        self.numar_porti_imbarcare - numar_porti_imbarcare
        self.pasageri_in_terminal = []
        
    def inscriere_pasager(self, nume_pasager):
        self.pasageri_in_terminal.append(nume_pasager)
        print(f"Pasagerul {nume_pasager} a fost inscris in terminalul {self.numar_terminal}.")
    
    def debarcare_pasager(self, nume_pasager):
        if nume_pasager in self.pasageri_in_terminal:
            self.pasageri_in_terminal.remove(nume_pasager)
            print(f"Pasagerul {nume_pasager} a fost debarcat din terminalul {self.numar_terminal}.")
        else:
            print(f"Pasagerul {nume_pasager} nu exista in terminalul {self.numar_terminal}.")