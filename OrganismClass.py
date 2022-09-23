
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
        elif num_of_organism is not None:
            self.unit_num = self.noo
        else:
            self.unit_num = acre * self.opa


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
        elif num_of_organism is not None:
            self.unit_num = self.noo
            
        else:
            self.unit_num = acre * self.opa


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
        elif num_of_organism is not None:
            self.unit_num = self.noo
            
        else:
            self.unit_num = acre * self.opa


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
        elif num_of_organism is not None:
            self.unit_num = self.noo
            
        else:
            self.unit_num = acre * self.opa


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
        elif num_of_organism is not None:
            self.unit_num = self.noo
            
        else:
            self.unit_num = acre * self.opa


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
        elif num_of_organism is not None:
            self.unit_num = self.noo
            
        else:
            self.unit_num = acre * self.opa
