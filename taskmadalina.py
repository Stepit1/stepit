class Zbor:
    def __init__(self, destinatie, oraplecarii, orasosirii):
        self.destinatie = destinatie
        self.oraplecarii = oraplecarii
        self.orasosirii = orasosirii
    def status(self):
        return f"destinatie este {self.destinatie}, ora plecarii este {self.oraplecarii} si ora sosirii este {self.orasosirii}"
    zbor = Zbor("milano", "11:00","12:45")
print(zbor.status())