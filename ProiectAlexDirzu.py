# *Task*: Definirea clasei principale (⁠ Aeroport ⁠)
#      - *Detalii*: Creați o clasă ⁠ Aeroport ⁠ pentru a gestiona informațiile de bază despre aeroport.
#      - *Cerințe*:
#        - Include atribute precum nume aeroport, cod IATA, locație (țară, oraș), și orice alte informații relevante.
#        - Implementează o metodă de inițializare (⁠ __init__ ⁠) pentru a seta aceste atribute.
#        - Asigură-te că ai o metodă pentru afișarea detaliilor aeroportului.



class Aeroport:
    def __init__(self, name, iata_code, country, city):
        self.name = name
        self.iata_code = iata_code
        self.country = country
        self.city = city
        self.no_terminals = no_terminals

    def display(self):
        print(f"Cel mai mare aeroport din sudul europei este {self.name}, acesta se afla in {self.country} orasul {self.city}. "
              f"Acesta are codul IATA {self.iata_code}.")

aeroport = Aeroport("Aeroportul International Henri Coanda", "OTP", "Romania", "Otopeni", 2)

aeroport.display()
