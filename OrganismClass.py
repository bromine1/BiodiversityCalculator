
class Organism:
    def __init__(self, mass_per_organism, num_of_organism, unit_num):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo
        if unit_num != None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class PP (Organism):
    def __init__(self, mass_per_organism, num_of_organism, unit_num):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo
        if unit_num != None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class PC (Organism):  # Primary Consumer
    def __init__(self, mass_per_organism, num_of_organism, unit_num):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo
        if unit_num != None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class SC (Organism):  # Secondary Consumer
    def __init__(self, mass_per_organism, num_of_organism, unit_num):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo
        if unit_num != None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class TC (Organism):  # Tertiary Consumer
    def __init__(self, mass_per_organism, num_of_organism, unit_num):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo
        if unit_num != None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class DP (Organism):
    def __init__(self, mass_per_organism, num_of_organism, unit_num):
        self.mpo = mass_per_organism
        self.noo = num_of_organism
        self.biomass = self.mpo * self.noo
        if unit_num != None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism
