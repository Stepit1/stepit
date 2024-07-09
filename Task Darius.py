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
terminal1 = aeroport.add_terminal("Terminal 1")
terminal2 = aeroport.add_terminal("Terminal 2")

flight1 = terminal1.add_flight("RO123", "Paris")
flight2 = terminal2.add_flight("RO456", "London")

flight1.add_passenger("John Doe")
flight1.add_passenger("Jane Doe")
flight2.add_passenger("Bob Smith")

aeroport.display_terminals()
terminal1.display_flights()
flight1.display_passengers()