
class Organism:  # make a data structure that contains attributes of organisms
    def __init__(self, mass_per_organism, organism_per_acre=None, acre=None,  num_of_organism=None, unit_num=None):
    # Line above defines accptable input
        self.mpo = mass_per_organism  # store the mass of an organism
        if num_of_organism is not None:
            self.noo = num_of_organism  # Store the number of organisms if one exists
            self.biomass = self.noo * self.mpo # calculate biomass by number
        if organism_per_acre is not None:
            self.opa = organism_per_acre  # store the number of organisms per acre
            self.biomass = self.mpo * acre * self.opa
            # multiply organisms per acre and the acres used
        if unit_num is not None:
            self.unit_num = unit_num # set unit if one exists
            # unit nums are used so 10,000 bees don't destroy the biodiversity
        elif num_of_organism is not None:
        # set unit num to other numbers, mainly the number of organisms
        # this allows the program to only reference the unit number
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
