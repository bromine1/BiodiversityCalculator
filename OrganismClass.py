
class Organism:
    def __init__(self, mass_per_organism, num_of_organism):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo


class PP (Organism):
    def __init__(self, mass_per_organism, num_of_organism):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo


class PC (Organism):  # Primary Consumer
    def __init__(self, mass_per_organism, num_of_organism):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo


class SC (Organism):  # Secondary Consumer
    def __init__(self, mass_per_organism, num_of_organism):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo


class TC (Organism):  # Tertiary Consumer
    def __init__(self, mass_per_organism, num_of_organism):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo


class DP (Organism):
    def __init__(self, mass_per_organism, num_of_organism):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo
