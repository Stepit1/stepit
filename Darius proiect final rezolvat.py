class Aeroport:
    def __init__(self, name, iata_code, country, city, no_terminals):
        self.name = name
        self.iata_code = iata_code
        self.country = country
        self.city = city
        self.no_terminals = no_terminals

    def display(self):
        print(f"Cel mai mare aeroport din sudul europei este {self.name}, acesta se afla in {self.country} orasul {self.city}. "
              f"Acesta are codul IATA {self.iata_code}.")

class Terminal(Aeroport):
    def __init__(self, nume_aeroport, cod_IATA, locatie, numar_terminal, numar_porti_imbarcare):
        super().__init__(nume_aeroport, cod_IATA, locatie, "", 0)  # Initialize Aeroport attributes
        self.numar_terminal = numar_terminal
        self.numar_porti_imbarcare = numar_porti_imbarcare
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

class Zbor:
    def __init__(self, destinatie, oraplecarii, orasosirii):
        self.destinatie = destinatie
        self.oraplecarii = oraplecarii
        self.orasosirii = orasosirii
    def status(self):
        return f"destinatie este {self.destinatie}, ora plecarii este {self.oraplecarii} si ora sosirii este {self.orasosirii}"

aeroport = Aeroport("Aeroportul International Henri Coanda", "OTP", "Romania", "Otopeni", 2)
aeroport.display()

terminal = Terminal("Aeroportul International Henri Coanda", "OTP", "Romania, Otopeni", 1, 20)
terminal.inscriere_pasager("Ion Popescu")
terminal.debarcare_pasager("Ion Popescu")

zbor = Zbor("milano", "11:00","12:45")
print(zbor.status())

# Second part of the code
class Aeroport:
    def __init__(self, name):
        self.name = name
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

    def display_terminals(self):
        for terminal in self.terminals:
            print(f"Terminal {terminal.name} has {len(terminal.flights)} flights")

class Terminal:
    def __init__(self, name, aeroport):
        self.name = name
        self.aeroport = aeroport
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

    def display_flights(self):
        for flight in self.flights:
            print(f"Flight {flight.number} to {flight.destination} has {len(flight.passengers)} passengers")

class Zbor:
    def __init__(self, number, destination, terminal):
        self.number = number
        self.destination = destination
        self.terminal = terminal
        self.passengers = []

    def add_passenger(self, passenger_name):
        self.passengers.append(passenger_name)

    def get_passenger(self, passenger_name):
        if passenger_name in self.passengers:
            return passenger_name
        return None

    def display_passengers(self):
        for passenger in self.passengers:
            print(f"Passenger {passenger}")

# Example usage:
aeroport = Aeroport("Bucharest Henri Coanda")
terminal1
