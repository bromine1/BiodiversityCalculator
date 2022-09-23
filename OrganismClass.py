
class Organism:
    def __init__(self, mass_per_organism, organism_per_acre=None, acre=None,  num_of_organism=None, unit_num=None):
        self.mpo = mass_per_organism
        if num_of_organism is not None:
            self.noo = num_of_organism
            self.biomass = self.noo * self.mpo
        if organism_per_acre is not None:
            self.opa = organism_per_acre
            self.biomass = self.mpo * acre * self.opa
        if unit_num is not None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class PP (Organism):
    def __init__(self, mass_per_organism, organism_per_acre=None, acre=None,  num_of_organism=None, unit_num=None):
        self.mpo = mass_per_organism
        if num_of_organism is not None:
            self.noo = num_of_organism
            self.biomass = self.noo * self.mpo
        if organism_per_acre is not None:
            self.opa = organism_per_acre
            self.biomass = self.mpo * acre * self.opa
        if unit_num is not None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class PC (Organism):  # Primary Consumer
    def __init__(self, mass_per_organism, organism_per_acre=None, acre=None,  num_of_organism=None, unit_num=None):
        self.mpo = mass_per_organism
        if num_of_organism is not None:
            self.noo = num_of_organism
            self.biomass = self.noo * self.mpo
        if organism_per_acre is not None:
            self.opa = organism_per_acre
            self.biomass = self.mpo * acre * self.opa
        if unit_num is not None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class SC (Organism):  # Secondary Consumer
    def __init__(self, mass_per_organism, organism_per_acre=None, acre=None,  num_of_organism=None, unit_num=None):
        self.mpo = mass_per_organism
        if num_of_organism is not None:
            self.noo = num_of_organism
            self.biomass = self.noo * self.mpo
        if organism_per_acre is not None:
            self.opa = organism_per_acre
            self.biomass = self.mpo * acre * self.opa
        if unit_num is not None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class TC (Organism):  # Tertiary Consumer
    def __init__(self, mass_per_organism, organism_per_acre=None, acre=None,  num_of_organism=None, unit_num=None):
        self.mpo = mass_per_organism
        if num_of_organism is not None:
            self.noo = num_of_organism
            self.biomass = self.noo * self.mpo
        if organism_per_acre is not None:
            self.opa = organism_per_acre
            self.biomass = self.mpo * acre * self.opa
        if unit_num is not None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism


class DP (Organism):
    def __init__(self, mass_per_organism, organism_per_acre=None, acre=None,  num_of_organism=None, unit_num=None):
        self.mpo = mass_per_organism
        if num_of_organism is not None:
            self.noo = num_of_organism
            self.biomass = self.noo * self.mpo
        if organism_per_acre is not None:
            self.opa = organism_per_acre
            self.biomass = self.mpo * acre * self.opa
        if unit_num is not None:
            self.unit_num = unit_num
        else:
            self.unit_num = num_of_organism
