class Persoon:
    def __init__(self, naam):
        self.naam = naam

    def groet(self):
        print("Hallo" + " " + self.naam)


iemand = Persoon("iemand")


iemand.groet()
