
class Aeroport:
    def __init__(self, name, iata_code, country, city):
        self.name = name
        self.iata_code = iata_code
        self.country = country
        self.city = city
        self.terminals = []

    def add_terminal(self, terminal_name):
        terminal = Terminal(terminal_name, self)
        self.terminals.append(terminal)
        return terminal

    def get_terminal(self, terminal_name):
        for terminal in self.terminals:
            if terminal.name == terminal_name:
                return terminal
        return None
    def display(self):
        print(f"Nume aeroport: {self.name}, tara: {self.country}, oras: {self.city}. "
              f"Acesta are codul IATA: {self.iata_code}.")

aeroport = Aeroport("Aeroportul International Henri Coanda", "OTP", "Romania", "Otopeni")

aeroport.display()


class Terminal(Aeroport):
    def __init__(self, name, iata_code, country, city, terminal, number_of_gates):
        super().__init__(name, iata_code, country, city)
        self.terminal = terminal
        self.number_of_gates = number_of_gates
        self.pasageri_in_terminal = []
        self.flights = []

    def add_flight(self, flight_number, destination):
        flight = Zbor(flight_number, destination, self)
        self.flights.append(flight)
        return flight

    def get_flight(self, flight_number):
        for flight in self.flights:
            if flight.number == flight_number:
                return flight
        return None

    def inscriere_pasager(self, nume_pasager):
        self.pasageri_in_terminal.append(nume_pasager)
        print(f"Pasagerul {nume_pasager} a fost inscris in terminalul {self.numar_terminal}.")

    def debarcare_pasager(self, nume_pasager):
        if nume_pasager in self.pasageri_in_terminal:
            self.pasageri_in_terminal.remove(nume_pasager)
            print(f"Pasagerul {nume_pasager} a fost debarcat din terminalul {self.numar_terminal}.")
        else:
            print(f"Pasagerul {nume_pasager} nu exista in terminalul {self.numar_terminal}.")

    def display_passengers(self):
        for passenger in self.passengers:
            print(f"Passenger {passenger}")

class Zbor:
    def __init__(self, destinatie, oraplecarii, orasosirii):
        self.destinatie = destinatie
        self.oraplecarii = oraplecarii
        self.orasosirii = orasosirii
    def status(self):
        return f"destinatie este {self.destinatie}, ora plecarii este {self.oraplecarii} si ora sosirii este {self.orasosirii}"

zbor = Zbor("milano", "11:00","12:45")
print(zbor.status())

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






